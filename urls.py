#!/usr/bin/env python

import gzip
import json
import requests
import unicodecsv
from bs4 import BeautifulSoup

counts = {}

for line in gzip.open('tweets.json.gz'):
    tweet = json.loads(line)
    for url in tweet["entities"]["urls"]:
        if 'unshortened_url' in url:
            u = url['unshortened_url']
            counts[u] = counts.get(u, 0) + 1

sorted_urls = counts.keys()
sorted_urls.sort(lambda a, b: cmp(counts[b], counts[a]))

def title(url):
    title = ''
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content)
            if soup.title:
                title = soup.title.string
    except requests.exceptions.Timeout:
        pass
    except requests.exceptions.SSLError:
        pass

    return title

csv = unicodecsv.writer(open("urls.csv", "w"))
for url in sorted_urls:
    csv.writerow([url, title(url), counts[url]])

