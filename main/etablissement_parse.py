#!/usr/bin/env
# -*- coding: utf-8 -*-
import sys

from main.offices import (
    determine_industry_code_and_headquarters_office,
    prospect_office
    )

from nightcrawlers.france.fr_helpers import (
    remove_empty_values,
    fr_create_dataframe
    )

from utils.pandas.dataframe_tools import (
    map_row_values, 
    pandas_dataframe
    )

from main.mappings import mappings
from main.etablissement_post_process import etablissement_post_process
from utils.dask.pandas_to_dask import iterate_dataframe
from utils import send_prospect_sources

establishment_mapping = mappings['etablissement']
source = 'etablissement'

download_index = sys.argv[1]


def parse():
    dataframe = pandas_dataframe(download_index, source)
    prospects = iterate_dataframe(dataframe, parse_row)

    for prospect_data in prospects:
        prospect = remove_empty_values(prospect_data)
        prospect = fr_establishment_post_process(prospect)

        if 'industry_code' not in prospect:
            prospect = prospect_office(prospect)

        if 'industry_code' in prospect:
            prospect = determine_industry_code_and_headquarters_office(prospect)

        yield prospect

 
def parse_row(row):
    return map_row_values(row, establishment_mapping)


if __name__ == "__main__":
    prospect = parse()
    send_prospect_sources('fr_etablissement', os.environ['SEND_KEY'], prospect)
