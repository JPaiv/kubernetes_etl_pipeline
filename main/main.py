#!/usr/bin/env
# -*- coding: utf-8 -*-

import sys
from utils.pandas_tools.dataframe_chunkers import chunk_csv_to_s3_create_kubejob_for_each_chunk
from main.helpers import (
    define_kubernetes_arguments,
    download_data_file
    )

source = sys.argv[1]


def main():
    data_file = download_data_file(source)
    kubernetes_args = define_kubernetes_arguments(source)
    chunk_csv_to_s3_create_kubejob_for_each_chunk(source, data_file, kubernetes_args, limits={'cpu': '1', 'memory': '4Gi'}, requests={'cpu': '1', 'memory': '2Gi'})


if __name__ == "__main__":
    main()
