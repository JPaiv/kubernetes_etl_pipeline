import logging
import boto3
import tempfile
import os
import re
#pylint: disable=import-error, no-name-in-module
from nightcrawlers.utils.s3.s3_helpers import form_upload_file_name, create_upload_key
#import pdb; pdb.set_trace()


logging.getLogger().setLevel("INFO")
TEMP_DIR = tempfile.mkdtemp()
s3 = boto3.client('s3')


def upload_basic_data_to_s3(folders, file_name, key_location_data_type=None, bucket='vainu-us-states-crawled'):
    """
        Requires a path to a folder. Use when downloading files with directory paths.
    """
    s3 = boto3.client('s3')
    key = '{}/{}'.format(folders, str(key_location_data_type))
    logging.info('Upload to s3: %s', key)
    s3.upload_file(file_name, bucket, key)


def download_basic_data_from_s3(folders, key, download_location_name, bucket='vainu-us-states-crawled'):
    """
        Requires a path to a folder. Use when downloading files with directory paths.
    """
    s3 = boto3.client('s3')
    key = '{}/{}'.format(folders, key)
    logging.info('Downloading file from s3: %s', key)
    s3.download_file(bucket, key, TEMP_DIR + '/{}'.format(str(download_location_name)))
    return TEMP_DIR + '/{}'.format(str(download_location_name))


def download_single_file_from_s3(key, download_location_name, bucket='vainu-us-states-crawled'):
    """
        Use download a single file from s3 with any folder path
    """
    s3 = boto3.client('s3')
    logging.info('Downloading file from s3: %s', key)
    s3.download_file(bucket, key, TEMP_DIR + '/{}'.format(str(download_location_name)))
    return TEMP_DIR + '/{}'.format(str(download_location_name))


def upload_fileobject_to_s3(folders, file_name, key_location_data_type=None, bucket='vainu-us-states-crawled'):
    s3 = boto3.client('s3')
    key = '{}/{}'.format(folders, str(key_location_data_type))
    logging.info('Upload to s3: %s', key)
    s3.upload_fileObj(file_name, bucket, key)


def download_fileobject_from_s3(folders, key, download_location_name, bucket='vainu-us-states-crawled'):
    s3 = boto3.client('s3')
    key = '{}/{}'.format(folders, key)
    logging.info('Downloading file from s3: %s', key)
    s3.download_file(bucket, key, TEMP_DIR + '/{}'.format(str(download_location_name)))
    return TEMP_DIR + '/{}'.format(str(download_location_name))


def delete_basic_data_from_s3(folders, delete_key, bucket='vainu-us-states-crawled'):
    """
        Use a path like structure with the folders
    """
    s3 = boto3.client('s3')
    key = '{}/{}'.format(folders, str(delete_key))
    s3.delete_object(Bucket=bucket, Key=key)
    logging.info('Deleted file from s3: %s', key)


def upload_directory_to_s3(folders, upload_directory, bucket='vainu-us-states-crawled'):
    s3 = boto3.client('s3')

    for file_name in os.listdir(upload_directory):
        upload_file_name = form_upload_file_name(upload_directory, file_name)
        key = create_upload_key(folders, file_name)
        logging.info('Upload to s3: %s', upload_file_name)
        s3.upload_file(upload_file_name, bucket, key)


def download_entire_folder(folders, bucket='vainu-us-states-crawled'):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket)

    for object in bucket.objects.filter(Prefix=folders):
        if not os.path.exists(os.path.dirname(TEMP_DIR + '/' + object.key)):
            os.makedirs(os.path.dirname(TEMP_DIR + '/' + object.key))

        bucket.download_file(object.key, TEMP_DIR + '/' + object.key)

    logging.info('File download complete, folder has been downloaded!')

    return TEMP_DIR


def get_all_s3_keys(bucket, key_prefix):
    keys = []
    kwargs = {
        'Bucket': bucket,
        'Prefix': key_prefix
        }

    while True:
        resp = s3.list_objects_v2(**kwargs)
        if resp.get('Contents'):
            for obj in resp['Contents']:
                keys.append(obj['Key'])
            try:
                kwargs['ContinuationToken'] = resp['NextContinuationToken']
            except KeyError:
                break
        else:
            logging.warning('No keys found')
            return []

    return keys


def download_all_matching_keys_from_s3(key_prefix, regex_match_pattern, bucket='vainu-us-states-crawled', download_to_directory=None):
    """
    Download all S3 objects whose key matches the given regex pattern.
    To avoid huge request loops to buckets with millions of keys, key_prefix is a required parameter and limits the possible keys to ones that start with that prefix.
    As default, the objects are downloaded into a new temp directory, with their original filenames.

    Example:
    To download all XML objects with 'norway-brreg-financial-xml/20190920/' in their key, pass...
    key_prefix = norway-brreg-financial-xml
    regex_match_pattern = 'norway-brreg-financial-xml/20190920/.*.xml'.

    Return a list of created file paths.
    """
    def get_matching_keys():
        keys = get_all_s3_keys(bucket, key_prefix)
        return [key for key in keys if re.search(regex_match_pattern, key)]

    def parse_filename(key):
        return key.split('/')[-1]

    keys = get_matching_keys()
    filepaths = []

    if not download_to_directory:
        download_to_directory = TEMP_DIR

    for key in keys:
        filename = parse_filename(key)
        download_to = '{}/{}'.format(download_to_directory, filename)
        logging.info('Downloading file from s3: %s', key)
        s3.download_file(bucket, key, download_to)
        filepaths.append(download_to)

    return list(set(filepaths))
