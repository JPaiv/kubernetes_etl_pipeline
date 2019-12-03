#!/usr/bin/env
# -*- coding: utf-8 -*-


STATIC_DICTS = {

    'fr_etablissement': {
    'country': 'FR',
    'source': 'sirene_etablissement_data',
    'target': 'prospect'
    },

    'fr_legale': {
        'country': 'FR',
        'source': 'sirene_legale_data',
        'target': 'prospect'
    }
}

mappings = {
    'fr_etablissement': {
    'siret': 'office_number',
    'siren': 'business_id',
    'dateCreationEtablissement': 'office_foundation_date',
    'enseigne1Etablissement': 'office_name',
    'enseigne2Etablissement': 'office_name_2',
    'enseigne3Etablissement': 'office_name_3',
    'codePostalEtablissement': 'office_postal',
    'libelleVoieEtablissement': 'office_address',
    'complementAdresseEtablissement': 'office_address_2',
    'complementAdresse2Etablissement': 'office_address_3',
    'numeroVoieEtablissement': 'office_address_number',
    'typeVoieEtablissement': 'office_address_type',
    'activitePrincipaleEtablissement': 'industry_code',
    'etatAdministratifEtablissement': 'status',
    'libelleCommuneEtablissement': 'office_municipality',
    'trancheEffectifsEtablissement': 'staff_number',
    'next_id': 'next_id'
    },

    'fr_legale': {
        'siren': 'business_id',
        'dateCreationUniteLegale': 'foundation_date',
        'denominationUniteLegale': 'company_name',
        'prenom1UniteLegale': 'company_name_first_name',
        'nomUniteLegale': 'company_name_last_name',
        'trancheEffectifsUniteLegale': 'staff_number',
        'activitePrincipaleUniteLegale': 'industry_code',
        'etatAdministratifUniteLegale': 'status',
        'categorieJuridiqueUniteLegale': 'form_of_company'
    }
}

employees = {
        'NN': {'lower_limit':0, 'upper_limit': 0},
        '00': {'lower_limit': 0, 'upper_limit': 0},
        '01': {'lower_limit': 1, 'upper_limit': 2},
        '02': {'lower_limit':3, 'upper_limit': 5},
        '03': {'lower_limit':6, 'upper_limit': 9},
        '11': {'lower_limit': 10, 'upper_limit': 19},
        '12': {'lower_limit': 20, 'upper_limit': 49},
        '21': {'lower_limit': 50, 'upper_limit': 99},
        '22': {'lower_limit': 100, 'upper_limit': 199},
        '31': {'lower_limit': 200, 'upper_limit': 249},
        '32': {'lower_limit': 250, 'upper_limit': 499},
        '41': {'lower_limit': 500, 'upper_limit': 999},
        '42': {'lower_limit': 1000, 'upper_limit': 1999},
        '51': {'lower_limit': 2000, 'upper_limit': 4999},
        '52': {'lower_limit': 5000, 'upper_limit': 9999},
        '53': {'lower_limit': 10000, 'upper_limit': 20000}
    }


address_types = {
        'ALL': 'Allée',
        'AV': 'Avenue',
        'BD': 'Boulevard',
        'CAR': 'Carrefour',
        'CHE': 'Chemin',
        'CHS': 'Chaussée',
        'CITE': 'Cité',
        'COR': 'Corniche',
        'CRS': 'Cours',
        'DOM': 'Domaine',
        'DSC': 'Descente',
        'ECA': 'Ecart',
        'ESP': 'Esplanade',
        'FG': 'Faubourg',
        'GR': 'Grande Rue',
        'HAM': 'Hameau',
        'HLE': 'Halle',
        'IMP': 'Impasse',
        'LD': 'Lieu dit',
        'LOT': 'Lotissement',
        'MAR': 'Marché',
        'MTE': 'Montée',
        'PAS': 'Passage',
        'PL': 'Place',
        'PLN': 'Plaine',
        'PLT': 'Plateau',
        'PRO': 'Promenade',
        'PRV': 'Parvis',
        'QUA': 'Quartier',
        'QUAI': 'Quai',
        'RES': 'Résidence',
        'RLE': 'Ruelle',
        'ROC': 'Rocade',
        'RPT': 'Rond Point',
        'RTE': 'Route',
        'RUE': 'Rue',
        'SEN': 'Sente-Sentier',
        'SQ': 'Square',
        'TPL': 'Terre-plein',
        'TRA': 'Traverse',
        'VLA': 'Villa',
        'VLGE': 'Village'
    }

etablissement_status = {
        'F': 'Fermé',
        'A': 'Actif'
    }

legale_status = {
        'C': 'Cessée',
        'A': 'Actif'
    }

region_mappings = {
    "Auvergne-Rhone-Alpes": "FR-ARA",
    "Bourgogne-Franche-Comté": "FR-BFC",
    "Bretagne": "FR-BRE",
    "Centre-Val de Loire": "FR-CVL",
    "Corse": "FR-COR",
    "Grand-Est": "FR-GES",
    "Guadeloupe": "FR-GUA",
    "Hauts-de-France": "FR-HDF",
    "Ile-de-France": "FR-IDF",
    "Mayotte": "FR-MAY",
    "Normandie": "FR-NOR",
    "Nouvelle-Aquitaine": "FR-NAQ",
    "Aquitaine-Limousin-Poitou-Charentes": "FR-NAQ",
    "Occitanie": "FR-OCC",
    "Pays-de-la-Loire": "FR-PDL",
    "Provence-Alpes-Cote d'Azur": "FR-PAC",
    "La Réunion":  "FR-LRE"
}
