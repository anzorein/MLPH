# MIT License

# Copyright (c) 2020 Santiago Anzorena

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import csv
import os.path
import requests
from datetime import date
from bs4 import BeautifulSoup

cwd = os.getcwd()
with open(f"{cwd}/links.txt", 'r', encoding='utf-8') as file:
	contents = file.readlines()
contents = [x.strip() for x in contents]
url_list = [line for line in contents if "https" in line if not "# https" in line]
name_list = [line.partition("= ")[2] for line in contents if "name =" in line if not "# name" in line]
name_list.insert(0,'Date')
price = [date.today()]
for url in url_list:
    website_html = requests.get(url).text
    parsed_html = BeautifulSoup(website_html, 'html.parser')
    price_list = []
    for price_tag in parsed_html.find_all(class_="price-tag-fraction"):
        price_list.append(price_tag.contents)
    price.append(min(price_list[0]))
if os.path.isfile(f"{cwd}/price-history.csv"):
    # file exists, add row with new values
    with open(f"{cwd}/price-history.csv", "a", newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';', dialect='excel')
        filewriter.writerow(price)
else: 
    # file doesnt exist, create it
    with open(f"{cwd}/price-history.csv", 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';', dialect='excel')
        filewriter.writerow(name_list)
        filewriter.writerow(price)
