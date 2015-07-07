# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
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
        content = output[0].encode('utf-8')
        encoding = output[1].encode('utf-8')
    return content, encoding


def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, 'html5lib', from_encoding=encoding)
    return parsed


def extract_data_listings(html):
    id_finder = re.compile(r'PR[\d]+~')
    return html.find_all('div', id=id_finder)


def has_two_tds(element):
    is_tr = element.name == 'tr'
    td_children = element.find_all('td', recursive=False)
    has_two = len(td_children) == 2
    return is_tr and has_two


def clean_data(td):
    data = td.string
    try:
        return data.strip(" \n:-")
    except AttributeError:
        return u""


if __name__ == '__main__':
    kwargs = {
        'Inspection_Start': '2/1/2013',
        'Inspection_End': '2/1/2015',
        'Zip_Code': '98109'
    }
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html, encoding = load_inspection_page()
    else:
        html, encoding = get_inspection_page(**kwargs)
    doc = parse_source(html, encoding)
    listings = extract_data_listings(doc)
    for listing in listings[:5]:
        metadata_rows = listing.find('tbody').find_all(
            has_two_tds, recursive=False
            )
        for row in metadata_rows:
            for td in row.find_all('td', recursive=False):
                print repr(clean_data(td))
            print
        print
    # print len(metadata_rows)
    # print len(listings)
    # print listings[0].prettify()
