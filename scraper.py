# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import json

INSPECTION_DOMAIN_NAME = b'http://info.kingcounty.gov'
INSPECTION_PATH = b'/health/ehs/foodsafety/inspections/Results.aspx'
INSPECTION_PARAMETERS = {'Output': 'W',
                         'Business_Name': '',
                         'Business_Address': '',
                         'Longitude': '',
                         'Latitude': '',
                         'City': '',
                         'Zip_Code': '',
                         'Inspection_Type': 'All',
                         'Inspection_Start': '',
                         'Inspection_End': '',
                         'Inspection_Closed_Business': 'A',
                         'Violation_Points': '',
                         'Violation_Red_Points': '',
                         'Violation_Descr': '',
                         'Fuzzy_Search': 'N',
                         'Sort': 'B'
                         }


def get_inspection_page(**kwargs):
    url = INSPECTION_DOMAIN_NAME + INSPECTION_PATH
    params = INSPECTION_PARAMETERS.copy()
    for key, val in kwargs.items():
        if key in INSPECTION_PARAMETERS:
            params[key] = val
    response = requests.get(url, params=params)
    return response.content, response.encoding


def load_inspection_page():
    with open('output.json') as data_file:
        output = json.load(data_file)
    return output


if __name__ == "__main__":
    output = get_inspection_page(Zip_Code=98121)
    print output
