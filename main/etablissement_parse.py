#!/usr/bin/env
# -*- coding: utf-8 -*-
import sys
#pylint: disable=import-error, no-name-in-module
from nightcrawlers.france.basic_data.fr_offices import \
    determine_industry_code_and_headquarters_office, \
    prospect_office

from nightcrawlers.france.fr_helpers import \
    remove_empty_values, \
    fr_create_dataframe

from nightcrawlers.france.basic_data.fr_mappings import mappings
from nightcrawlers.france.basic_data.etablissement_post_process import fr_establishment_post_process
from nightcrawlers.utils.dask.pandas_to_dask import iterate_dataframe
from nightcrawlers.utils.pandas_tools.dataframe_tools import map_row_values
from nightcrawlers.utils import send_prospect_sources

establishment_mapping = mappings['fr_etablissement']
source = 'fr_etablissement'

download_index = sys.argv[1]


def parse():
    dataframe = fr_create_dataframe(download_index, source)
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
    send_prospect_sources('fr_etablissement', 'NmFjM9aDzqmnytPktdHJtRsC3jdE5uSKLutQGNfikDZ9QfiRvnPt2ns2CQORcog8rRkummY681X2jbbMw3nhjruwIUs_', prospect)
