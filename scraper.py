# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import json
from bs4 import BeautifulSoup
import sys
import re


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


def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, 'html5lib', from_encoding=encoding)
    return parsed


def extract_data_listings(html):
    id_finder = re.complie(r'PR[\d]+~')
    return html.findall('div', id=id_finder)


if __name__ == "__main__":
    for arg in sys.argv:
        if arg == "test":
            load_inspection_page()
            print 'test'
        else:
            get_inspection_page(Zip_Code=98121)
