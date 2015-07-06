# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

# url = ('http://info.kingcounty.gov/health/ehs/foodsafety/inspections/Results.'
#        'aspx?Output=W&Business_Name=&Business_Address=&Longitude=&Latitude=&C'
#        'ity=Seattle&Zip_Code=98121&Inspection_Type=All&Inspection_Start=&Insp'
#        'ection_End=&Inspection_Closed_Business=A&Violation_Points=&Violation_'
#        'Red_Points=&Violation_Descr=&Fuzzy_Search=N&Sort=B')
domain_name = b'http://info.kingcount.gov'
path = b'/health/ehs/foodsafety/inspections/Results.aspx'
parameters = {b'Output': b'W',
              b'Business_Name': b'',
              b'Business_Address': b'',
              b'Longitude': b'',
              b'Latitude': b'',
              b'City': b'Seattle',
              b'Zip_Code': b'98121',
              b'Inspection_Type': b'All',
              b'Inspection_Start': b'',
              b'Inspection_End': b'',
              b'Inspection_Closed_Business': b'A',
              b'Violation_Points': b'',
              b'Violation_Red_Points': b'',
              b'Violation_Descr': b'',
              b'Fuzzy_Search': b'N',
              b'Sort': b'B',
              }


def get_inspection_page(url=None, **kwargs):
    url = domain_name + path
    params = parameters.copy()
    for key, val in kwargs.iteritems():
        if key in parameters:
            params[key] = val
    response = requests.get(url, params=params)
    return response.content, response.encoding

if __name__ == "__main__":
    output = get_inspection_page(parameters)
    print output
