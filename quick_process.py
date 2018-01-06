#!/usr/bin/python3
import os
import sys

import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify the data dir.")
        exit()
    DATA_DIR = sys.argv[1]
    if not os.path.isdir(DATA_DIR):
        print("Path %s is not a valid directory" % DATA_DIR)
        exit()
    DATA_FILE = DATA_DIR.rstrip('/') + '/' + 'cities15000.txt'
    if not os.path.exists(DATA_FILE):
        print("Data file %s doesn't exist." % DATA_FILE)
        exit()

    # See http://download.geonames.org/export/dump/readme.txt for descriptions of the data fields.
    COLUMN_NAMES = [
        'geonameid',      # integer id of record in geonames database
        'name',           # name of geographical point (utf8) varchar(200)
        # name of geographical point in plain ascii characters, varchar(200)
        'asciiname',
        # alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
        'alternatenames',
        'latitude',       # latitude in decimal degrees (wgs84)
        'longitude',      # longitude in decimal degrees (wgs84)
        # see http://www.geonames.org/export/codes.html, char(1)
        'feature class',
        # see http://www.geonames.org/export/codes.html, varchar(10)
        'feature code',
        'country code',   # ISO-3166 2-letter country code, 2 characters
        'cc2',            # alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
        # fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
        'admin1 code',
        # code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80)
        'admin2 code',
        # code for third level administrative division, varchar(20)
        'admin3 code',
        # code for fourth level administrative division, varchar(20)
        'admin4 code',
        'population',     # bigint (8 byte int)
        'elevation',      # in meters, integer
        # digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
        'dem',
        # the iana timezone id (see file timeZone.txt) varchar(40)
        'timezone',
        'modification date',  # date of last modification in yyyy-MM-dd format
    ]
    city_data = pd.read_csv(DATA_FILE, sep='\t', header=None, names=COLUMN_NAMES)
    city_data = city_data[[
        'geonameid', 'name', 'asciiname', 'alternatenames', 'latitude',
        'longitude', 'country code', 'admin1 code', 'admin2 code',
        'population', 'elevation', 'timezone']]
    print("Data size:", city_data.shape)
    print(city_data[city_data['asciiname'] == 'New York City'])
