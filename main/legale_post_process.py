#!/usr/bin/env
# -*- coding: utf-8 -*-


from nightcrawlers.france.basic_data.fr_mappings import (
    employees,
    legale_status
    )


def post_process_legale(prospect_data):
    prospect_data = create_business_id(prospect_data)
    prospect_data = status(prospect_data)
    prospect_data = combine_company_names(prospect_data)
    prospect_data = staff_number(prospect_data)
    prospect_data = industry_code(prospect_data)
    prospect_data = delete_obsolete_values(prospect_data)

    return prospect_data


def create_business_id(prospect_data):
    prospect_data['business_id'] = 'FR' + prospect_data['business_id']

    return prospect_data


def status(prospect_data):
    if 'status' in prospect_data:
        prospect_data['status'] = legale_status[prospect_data['status']]

    return prospect_data


def combine_company_names(prospect_data):
    if 'company_name' not in prospect_data:
        if 'company_name_first_name' in prospect_data and 'company_name_last_name' in prospect_data:
            prospect_data['company_name'] = prospect_data['company_name_first_name'] + ' ' + prospect_data['company_name_last_name']

    return prospect_data


def staff_number(prospect_data):
    if 'staff_number' in prospect_data:
        if prospect_data['staff_number'] != 'NN':
            staff_number_lowerlimit = employees[prospect_data['staff_number']]
            prospect_data['staff_number_lowerlimit'] = staff_number_lowerlimit['lower_limit']

            staff_number_upperlimit = employees[prospect_data['staff_number']]
            prospect_data['staff_number_upperlimit'] = staff_number_upperlimit['upper_limit']

    return prospect_data


def industry_code(prospect_data):
    if 'industry_code' in prospect_data:
        industry_code = prospect_data['industry_code'].replace(".", "")
        industry_code = {'code': industry_code, "code_scheme": "fr_naf_2008"}
        prospect_data['industry_codes'] = []
        prospect_data['industry_codes'].append(industry_code)

    return prospect_data


def delete_obsolete_values(prospect_data):
    legale_del_list = ['staff_number', 'company_name_first_name', 'company_name_last_name', 'industry_code', 'trancheeffectifsunitelegale', 'activiteprincipaleunitelegale', 'caractereemployerunitelegale']

    for item in legale_del_list:
        if item in prospect_data:
            del prospect_data[item]

    return prospect_data
