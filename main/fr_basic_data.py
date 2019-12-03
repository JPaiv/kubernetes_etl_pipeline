#!/usr/bin/env
# -*- coding: utf-8 -*-
import sys
#pylint: disable=import-error, no-name-in-module
from nightcrawlers.utils.pandas_tools.dataframe_chunkers import chunk_csv_to_s3_create_kubejob_for_each_chunk
from nightcrawlers.france.fr_helpers import define_kubernetes_arguments, download_data_file
#import pdb; pdb.set_trace()


source = sys.argv[1]


def basic_data():
    data_file = download_data_file(source)

    kubernetes_args = define_kubernetes_arguments(source)

    chunk_csv_to_s3_create_kubejob_for_each_chunk(source, data_file, kubernetes_args, limits={'cpu': '1', 'memory': '4Gi'}, requests={'cpu': '1', 'memory': '2Gi'})


if __name__ == "__main__":
    basic_data()
