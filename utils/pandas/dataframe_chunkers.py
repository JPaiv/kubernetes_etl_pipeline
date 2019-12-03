import tempfile
import pandas as pd
import logging
import time
from utils.s3.s3_tools import upload_basic_data_to_s3
from utils.kubejob import create_kube_job

TEMP_DIR = tempfile.mkdtemp()
logging.getLogger().setLevel("INFO")


def chunk_to_csv_upload_s3_create_kubejob(index, chunk, sep=',', **kwargs):
    """
        Turns the preferably small dataframe into a CSV file which is uploaded to AWS s3.
    """

    index = str(index)
    chunk.to_csv(TEMP_DIR + '/{}_data_chunk_{}.csv'.format(kwargs['source'], index), sep=sep)

    upload_basic_data_to_s3(kwargs['source'], TEMP_DIR + '/{}_data_chunk_{}.csv'.format(kwargs['source'], index), 'data_{}.csv'.format(index))

    source = kwargs['source'].replace('_', '-')
    kubernetes_args = kwargs['kubernetes_args']
    create_kube_job(source, kubernetes_args, index)


def chunk_csv_to_s3_create_kubejob_for_each_chunk(source, dataframe_file, kubernetes_args, dtype=str, error_bad_lines=False, quoting=0, encoding='utf-8', index_col=None, sep=',', limits=None, requests=None, chunksize=1000000):
    """
        Creates a pandas dataframe with default values from a CSV/TXT file which is chunked into a 1 million row long smaller dataframes. The pieces are then downloaded into AWS s3.
        Function also starts a kubernetes job for each chunk.
    """

    logging.info('Start chunking')

    for index, chunk in enumerate(pd.read_csv(dataframe_file, dtype=dtype, sep=sep, error_bad_lines=error_bad_lines, encoding=encoding, index_col=index_col, quoting=quoting, chunksize=chunksize)):
        index = str(index)
        logging.info('Dataframe csv chunk index: %s', index)

        chunked_dataframe_to_csv_and_upload_to_s3(chunk, source, index)

        #Append chunk index to kubejob args so kubejob will be numered so kubejob will have the same index number as the chunk
        kubernetes_args.append(index)
        create_kube_job(source, kubernetes_args, index, limits=limits, requests=requests)

        #Remove kubejob index to prevent duplicates
        del kubernetes_args[-1]

        limit_number_of_kubejobs_to_15(index)


def chunked_dataframe_to_csv_and_upload_to_s3(chunk, source, index):
    """
        Turn the chunked pandas dataframe into a CSV file which is uploaded to s3.
    """

    chunk.to_csv(TEMP_DIR + '/{}_data_chunk_{}.csv'.format(source, index), sep=',')
    upload_basic_data_to_s3(source, TEMP_DIR + '/{}_data_chunk_{}.csv'.format(source, index), 'data_{}.csv'.format(index))


def limit_number_of_kubejobs_to_15(index):
    """
        Limits number of simultaneous kubejob to 15 to prevent overcapacity
    """

    if int(index) % 15 == 0 and int(index) != 0:
        time.sleep(60*45)
