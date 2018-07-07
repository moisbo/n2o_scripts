#! /bin/python

from bs4 import BeautifulSoup
import wget
import requests
import os
import sys


def main():

    # specify the url
    if not len(sys.argv) > 1:
        print "Please include url in the form of http://www.N2O.net.au/knb/metacat/bel.18.25/html"
        print "to download files in that package"
        print "Example: "
        print "python download_packages.py http://www.N2O.net.au/knb/metacat/bel.18.25/html"
        print "_____"
        exit()

    param_1 = sys.argv[1]

    url = param_1
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    theOUrl = 'dUrl_'
    theSelect = 'div[id^="' + theOUrl + '"]'

    downloads = soup.select(theSelect)

    for tag in downloads:
        print tag.text
        download(tag.text)


def download(url):
    dir = os.path.join(os.getcwd(), 'download')
    wget.download(url, dir)


if __name__ == '__main__':
    main()
