#!/usr/bin/env
# -*- coding: utf-8 -*-
from utils.download_tools import download_file
from utils.download_tools import download_zip_endswith



def define_kubernetes_arguments(source):
    if source == 'legale':
        parser_name = 'legale_parse'
        subdir = 'basic_data'
    if source == 'etablissement':
        subdir = 'basic_data'
        parser_name = 'etablissement_parse'

    kubernetes_arguments = ['-m', 'nightcrawlers.france.{}.{}'.format(subdir, parser_name)]

    return kubernetes_arguments
    
    
def legal_category_download():
    legal_category_data = download_file('https://www.insee.fr/fr/statistiques/fichier/2028129/cj_juillet_2018.xls', 'xls')

    df_legal_category = pd.read_excel(legal_category_data, index=False, sheet_name='Niveau I', header=3, encoding='utf-8')
    df_legal_category_2 = pd.read_excel(legal_category_data, index=False, sheet_name='Niveau II', header=3, encoding='utf-8')
    df_legal_category_3 = pd.read_excel(legal_category_data, index=False, sheet_name='Niveau III', header=3, encoding='utf-8')
    df_legal_category = df_legal_category.append(df_legal_category_2)
    df_legal_category = df_legal_category.append(df_legal_category_3)
    legal_category_data = df_legal_category.groupby('Code')[u'Libell\xe9'].apply(list).to_dict()

    return legal_category_data
    
 def download_data_file(source):
    if source == 'legale':
        data_file = download_zip_endswith('https://www.data.gouv.fr/en/datasets/r/f5e54ead-987c-4db2-8a23-59aa210af41c', '.csv')

    if source == 'etablissement':
        data_file = download_zip_endswith('https://www.data.gouv.fr/en/datasets/r/b1cb58fd-0b05-4489-ad18-47765a2b08b1', '.csv')

    return data_file
