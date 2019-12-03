#!/usr/bin/env
# -*- coding: utf-8 -*-
import sys
#pylint: disable=import-error, no-name-in-module
from nightcrawlers.france.fr_helpers import \
    fr_create_dataframe, \
    remove_empty_values, \
    give_form_of_company, \
    legal_category_download

from nightcrawlers.france.basic_data.fr_mappings import mappings
from nightcrawlers.utils.dask.pandas_to_dask import iterate_dataframe
from nightcrawlers.france.basic_data.legale_post_process import post_process_fr_legale
from nightcrawlers.utils.pandas_tools.dataframe_tools import map_row_values
from nightcrawlers.utils import send_prospect_sources


legale_mapping = mappings['fr_legale']
source = 'fr_legale'

download_index = sys.argv[1]


def parse():
    dataframe = fr_create_dataframe(download_index, source)
    legal_category_data = legal_category_download()
    prospects = iterate_dataframe(dataframe, parse_row)

    for prospect_data in prospects:
        prospect_data = remove_empty_values(prospect_data)
        prospect_data = post_process_fr_legale(prospect_data)
        prospect_data = give_form_of_company(prospect_data, legal_category_data)

        if 'company_name' not in prospect_data:
            continue
        if 'company_name' in prospect_data:
            yield prospect_data


def parse_row(row):
    return map_row_values(row, legale_mapping)


if __name__ == "__main__":
    prospect = parse()
    send_prospect_sources('fr_legale_data', 'NDQ0N89NP3o07PGsqn58AIDA5ZQfOLk6md31_edTx5N5Lz0vcIWsirkuesvHCuLhOipNfP3LCgUs4X95qIqreluMyu8M', prospect)
