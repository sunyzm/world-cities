#!/bin/bash
cd "$(dirname "$0")"
curl -o ../data/country_info.txt http://download.geonames.org/export/dump/countryInfo.txt
curl -o ../data/cities15000.zip http://download.geonames.org/export/dump/cities15000.zip
unzip ../data/cities15000.zip -d ../data

