#!/usr/bin/env
# -*- coding: utf-8 -*-
#pylint: disable=import-error, no-name-in-module

from main.mappings import (
    employees,
    etablissement_status,
    address_types
)

from main.helpers import remove_empty_values 


def etablissement_post_process(prospect_data):
    prospect_data = remove_empty_values(prospect_data)
    prospect_data = office_address(prospect_data)
    prospect_data = office_name(prospect_data)
    prospect_data = staff_number(prospect_data)
    prospect_data = status(prospect_data)
    prospect_data = branch_number(prospect_data)
    prospect_data = office_number(prospect_data)
    prospect_data = business_id(prospect_data)
    prospect_data = delete_uncombined_values(prospect_data)

    return prospect_data


def office_address(prospect_data):
    if 'office_address' in prospect_data:
        if 'office_address_type' in prospect_data:
            if prospect_data['office_address_type'] in address_types:
                prospect_data['address'] = address_types[prospect_data['office_address_type']] + ' ' + prospect_data['office_address']
            else:
                prospect_data['address'] = prospect_data['office_address_type'] + ' ' + prospect_data['office_address']

            if 'address' in prospect_data and 'office_address_number' in prospect_data:
                prospect_data['address'] = prospect_data['office_address_number'] + ' ' + prospect_data['address']

            if 'address' in prospect_data and 'office_address_2' in prospect_data and 'office_address_3' not in prospect_data:
                prospect_data['address'] = prospect_data['address'] + " " + prospect_data['office_address_2']

            if 'address' in prospect_data and 'office_address_2' in prospect_data and 'office_address_3' in prospect_data:
                prospect_data['address'] = prospect_data['address'] + " " + prospect_data['office_address_2'] + " " + prospect_data['office_address_3']

        if 'office_address_type' not in prospect_data:
            if 'office_address' in prospect_data and 'office_address_2' in prospect_data and 'office_address_3' not in prospect_data:
                prospect_data['address'] = prospect_data['office_address'] + " " + prospect_data['office_address_2']

            if 'office_address' in prospect_data and 'office_address_2' in prospect_data and 'office_address_3' in prospect_data:
                prospect_data['address'] = prospect_data['office_address'] + " " + prospect_data['office_address_2'] + " " + prospect_data['office_address_3']

    return prospect_data


def office_name(prospect_data):
    if 'office_name' not in prospect_data and 'office_name_2' in prospect_data:
        prospect_data['office_name'] = prospect_data['office_name_2']

    if 'office_name' not in prospect_data and 'office_name_2' not in prospect_data and 'office_name_3' in prospect_data:
        prospect_data['office_name'] = prospect_data['office_name_3']

    if 'office_name' in prospect_data and 'office_name_2' in prospect_data and 'office_name_3' in prospect_data:
        prospect_data['office_name'] = prospect_data['office_name'] + " " + prospect_data['office_name_2'] + " " +  prospect_data['office_name_3']

    if 'office_name' in prospect_data and 'office_name_2' in prospect_data and 'office_name_3' not in prospect_data:
        prospect_data['office_name'] = prospect_data['office_name'] + " " + prospect_data['office_name_2']

    return prospect_data


def staff_number(prospect_data):
    if 'staff_number' in prospect_data:
        staff_number_lowerlimit = employees[prospect_data['staff_number']]
        prospect_data['staff_number_lowerlimit'] = staff_number_lowerlimit['lower_limit']

        staff_number_upperlimit = employees[prospect_data['staff_number']]
        prospect_data['staff_number_upperlimit'] = staff_number_upperlimit['upper_limit']

    return prospect_data


def status(prospect_data):
    if 'status' in prospect_data:
        prospect_data['status'] = etablissement_status[prospect_data['status']]

    return prospect_data


def branch_number(prospect_data):
    if 'branch_number' in prospect_data:
        prospect_data['branch_number'] = 'FR' + prospect_data['branch_number']

    return prospect_data


def office_number(prospect_data):
    if 'office_number' in prospect_data:
        prospect_data['office_number'] = 'FR' + prospect_data['office_number']

    return prospect_data


def business_id(prospect_data):
    if 'business_id' in prospect_data:
        if len(prospect_data['business_id']) == 9:
            prospect_data['business_id'] = 'FR' + prospect_data['business_id']

    return prospect_data


def delete_uncombined_values(prospect_data):
    etablissement_del_list = ['officename_2', 'officename_3', 'office_address_2', 'office_address_3', 'office_address_2', 'office_address_type', 'office_address_number', 'employer', 'staff_number']
    for item in etablissement_del_list:
        if item in prospect_data:
            del prospect_data[item]

    return prospect_data
