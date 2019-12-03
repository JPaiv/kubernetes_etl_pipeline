#!/usr/bin/env
# -*- coding: utf-8 -*-
#pylint: disable=import-error, no-name-in-module
from nightcrawlers.utils import send_prospect_sources


def delete_prospect():
    prospect = {
        'business_id': 'FR810245936',
        'status': 'Inactive',
        'country': 'FR',
        'target': 'prospect',
        'source': 'fr_legale_data'
    }

    yield prospect


if __name__ == "__main__":
    prospect = delete_prospect()
    send_prospect_sources('fr_legale_data', 'NDQ0N89NP3o07PGsqn58AIDA5ZQfOLk6md31_edTx5N5Lz0vcIWsirkuesvHCuLhOipNfP3LCgUs4X95qIqreluMyu8M', prospect)
