import pandas as pd
import numpy as np
import tensorflow as tf
#pylint: disable=import-error, no-name-in-module
from nightcrawlers.utils.s3.s3_tools import download_basic_data_from_s3
#import pdb; pdb.set_trace()


def map_row_values(row, mappings):
    """
        Used to map dataframe row during iteration for data parser.
    """

    prospect_data = {}
    for key, value in mappings.items():
        prospect_data[value] = row[key].strip()

    return prospect_data


def create_dataframe_from_chunked_csv(source, download_index, sep=',', encoding='utf-8', business_id_column=''):
    """
        Create a pandas dataframe with preset arguments form a chunked CSV file downloaded from AWS s3.
    """

    csv_file = download_basic_data_from_s3(source, 'data_{}.csv'.format(download_index), 'data.csv')
    dataframe = pd.read_csv(csv_file, dtype=str, sep=sep, encoding=encoding, error_bad_lines=False)
    dataframe = dataframe.replace(np.nan, '', regex=True)

    if business_id_column:
        dataframe = dataframe.dropna(subset=[business_id_column])

    return dataframe


def create_dataframe(source, download_index, sep=';', encoding='utf-8'):
    """
        Create pandas dataframe with preset values from s3 downloaded CSV file.
    """

    csv_file = download_basic_data_from_s3(source, 'data_{}.csv'.format(download_index), 'data.csv')
    dataframe = pd.read_csv(csv_file, dtype=str, sep=sep, encoding=encoding, error_bad_lines=False)
    dataframe = dataframe.replace(np.nan, '', regex=True)

    return dataframe


def pandas_dataframe(csv_file, dtype=str, sep=',', encoding='utf-8', quoting=0, index_col=None):
    """
        Create a new pandas dataframe from a CSV with preset arguments.
    """

    dataframe = pd.read_csv(csv_file, dtype=dtype, sep=sep, encoding=encoding, index_col=index_col, quoting=quoting, error_bad_lines=False)
    dataframe = dataframe.replace(np.nan, '', regex=True)

    return dataframe


def dataframe_to_dataset(dataframe, shuffle=True, batch_size=32):
    """
        Turn a pandas dataframe into a tensorflow dataset/tf.data dataset. Requires headers!
    """

    dataframe = dataframe.copy()
    dataset = tf.data.Dataset.from_tensor_slices((dict(dataframe)))
    if shuffle:
        dataset = dataset.shuffle(buffer_size=len(dataframe))
    dataset = dataset.batch(batch_size)

    return dataset
