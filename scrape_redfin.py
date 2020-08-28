from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import  logging
import process_csv

def generate_param(location_file_path, csv_delimiter):
    """convert csv data to root param format /code/state/city"""
    param_list = []
    input_list = process_csv.extract_csv_to_list(location_file_path, csv_delimiter=csv_delimiter)
    for row in input_list:
        param = '/{}/{}/{}{}'.format(*row)
        param_list.append(param)
    return param_list

def generate_filter_param(filter_dict = dict()):
    filter_param_list = []

    return filter_param_list


def html_from_request(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    request = Request(url, headers = headers)
    html = urlopen(request).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

if __name__ == '__main__':
    # execute only if run as a script
    file_path = 'C:/workspace/ProjectRedfinScrape/files/city_list.csv'
    delimiter = ','
    # print(generate_param(file_path, delimiter))
    html_from_request('https://www.redfin.com/city/7178/TX/Galveston/filter/property-type=house+condo+townhouse+multifamily,include=sold-3mo')