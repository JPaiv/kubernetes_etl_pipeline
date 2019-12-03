import logging

logging.getLogger().setLevel("INFO")


def form_upload_file_name(upload_directory, file_name):
    upload_file_name = '{}/{}'.format(upload_directory, file_name)

    return upload_file_name


def create_upload_key(source, file_name):
    key = source + '/' + file_name

    return key
