 #!/usr/bin/env
# -*- coding: utf-8 -*-
import requests
import zipfile
import tempfile
import logging
import os
import tarfile

logging.getLogger().setLevel("INFO")
TEMP_DIR = tempfile.mkdtemp()


def download_zip_endswith(url, listdir_file_endswith, verify=True):#pylint: disable=inconsistent-return-statements
    logging.info("Downloading zip with endswith-search")
    data = requests.get(url, verify=verify)

    logging.info(data.status_code)

    open(TEMP_DIR + '/download.zip', 'wb').write(data.content)
 
    logging.info('Unzip download.zip')

    with zipfile.ZipFile(TEMP_DIR + '/download.zip') as zip_ref_1:
        zip_ref_1.extractall(TEMP_DIR)

    for filename in os.listdir(TEMP_DIR):
        if filename.endswith(listdir_file_endswith):

            return TEMP_DIR + '/' + filename


def download_file(url, file_type, verify=True):
    logging.info("Downloading %s", file_type)
    data = requests.get(url, verify=verify)
    logging.info(data.status_code)
    open(TEMP_DIR + '/download.{}'.format(file_type), 'wb').write(data.content)

    return TEMP_DIR + '/download.{}'.format(file_type)





