#!/usr/bin/env
# -*- coding: utf-8 -*-
#import pdb; pdb.set_trace()


def determine_industry_code_and_headquarters_office(prospect_data):
    industry_code = prospect_data['industry_code']
    industry_code_scheme = {'code': industry_code, "code_scheme": "fr_naf_2008"}
    prospect_data = append_industry_code(prospect_data, industry_code_scheme)

    if industry_code[:2] == '70':
        if check_industry_code(industry_code) is True:
            prospect_data = give_headquarters_address_to_prospect(prospect_data)
            prospect_data = create_office_address(prospect_data, industry_code_scheme)
            prospect_data = delete_used_values_hq(prospect_data)
        else:
            prospect_data = create_office_address(prospect_data, industry_code_scheme)
            prospect_data = delete_used_values(prospect_data)

    else:
        prospect_data = create_office_address(prospect_data, industry_code_scheme)
        prospect_data = delete_used_values(prospect_data)

    return prospect_data


def check_industry_code(industry_code):
    return industry_code[:3] == '701'


def give_headquarters_address_to_prospect(prospect_data):
    if 'address' in prospect_data:
        prospect_data['visiting_address'] = prospect_data['address']
        if 'office_postal' in prospect_data:
            prospect_data['postal'] = prospect_data['office_postal']
            prospect_data['visiting_postal'] = prospect_data['postal']
        if 'office_municipality' in prospect_data:
            prospect_data['municipality'] = prospect_data['office_municipality']
            prospect_data['visiting_municipality'] = prospect_data['municipality']

    return prospect_data


def create_office_address(prospect_data, industry_code_scheme):
    office = {}
    if 'address' in prospect_data:
        office['address'] = prospect_data['address']
    if 'office_postal' in prospect_data:
        office['postal'] = prospect_data['office_postal']
    if 'office_municipality' in prospect_data:
        office['municipality'] = prospect_data['office_municipality']
    if 'office_number' in prospect_data:
        office['office_number'] = prospect_data['office_number']
    if 'office_name' in prospect_data:
        office['office_name'] = prospect_data['office_name']
    if 'status' in prospect_data:
        office['status'] = prospect_data['status']
    if 'office_foundation_date' in prospect_data:
        office['foundation_date'] = prospect_data['office_foundation_date']
    if 'staff_number_upperlimit' in prospect_data:
        office['staff_number_upperlimit'] = prospect_data['staff_number_upperlimit']
        del prospect_data['staff_number_upperlimit']
    if 'staff_number_lowerlimit' in prospect_data:
        office['staff_number_lowerlimit'] = prospect_data['staff_number_lowerlimit']
        del prospect_data['staff_number_lowerlimit']

    office['industry_codes'] = []
    office['industry_codes'].append(industry_code_scheme)

    if 'prospect_addresses' not in prospect_data:
        prospect_data['prospect_addresses'] = []
    prospect_data['prospect_addresses'].append(office)

    return prospect_data


def append_industry_code(prospect_data, industry_code_scheme):
    if 'industry_codes' not in prospect_data:
        prospect_data['industry_codes'] = []
    if industry_code_scheme not in prospect_data['industry_codes']:
        prospect_data['industry_codes'].append(industry_code_scheme)

    return prospect_data


def delete_used_values(prospect_data):
    for del_value in ['address', 'office_address', 'office_postal', 'office_municipality', 'office_number', 'industry_code', 'status', 'office_foundation_date']:
        if del_value in prospect_data:
            del prospect_data[del_value]

    return prospect_data


def delete_used_values_hq(prospect_data):
    for del_value in ['office_address', 'office_postal', 'office_municipality', 'office_number', 'industry_code', 'status', 'office_foundation_date']:
        if del_value in prospect_data:
            del prospect_data[del_value]

    return prospect_data


def prospect_office(prospect_data):
    office = {}
    if 'address' in prospect_data:
        office['address'] = prospect_data['address']
    if 'office_postal' in prospect_data:
        office['postal'] = prospect_data['office_postal']
    if 'office_municipality' in prospect_data:
        office['municipality'] = prospect_data['office_municipality']
    if 'office_number' in prospect_data:
        office['office_number'] = prospect_data['office_number']
    if 'office_name' in prospect_data:
        office['office_name'] = prospect_data['office_name']
    if 'status' in prospect_data:
        office['status'] = prospect_data['status']
    if 'office_foundation_date' in prospect_data:
        office['foundation_date'] = prospect_data['office_foundation_date']
    if 'staff_number_upperlimit' in prospect_data:
        office['staff_number_upperlimit'] = prospect_data['staff_number_upperlimit']
        del prospect_data['staff_number_upperlimit']
    if 'staff_number_lowerlimit' in prospect_data:
        office['staff_number_lowerlimit'] = prospect_data['staff_number_lowerlimit']
        del prospect_data['staff_number_lowerlimit']

    if 'prospect_addresses' not in prospect_data:
        prospect_data['prospect_addresses'] = []
    prospect_data['prospect_addresses'].append(office)

    prospect_data = delete_used_values(prospect_data)

    return prospect_data
