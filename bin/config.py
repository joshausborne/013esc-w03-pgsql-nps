#!/usr/bin/env python3

import json
import psycopg2
import os
import sys

base_dir = 'project_path/repo_directory/' # NEEDS UPDATING TO REFLECT YOUR ENVIRONMENT

conf_dir = os.path.join(base_dir,'conf/')
data = os.path.join(base_dir,'data/')
kml_dir = os.path.join(base_dir,'kml/')
boundaries = os.path.join(kml_dir,'boundaries/')
flytos = os.path.join(kml_dir,'flytos/')
placemarks = os.path.join(kml_dir,'placemarks/')
placemark_img = 'https://raw.githubusercontent.com/joshausborne/013esc-w03-pgsql-nps/main/images/placemark-star.png'


# Import DB connection credentials from nps_db_connect.json

with open(conf_dir + 'nps_db_connect.json','r') as f:
    creds = json.load(f)

host = creds['host']
dbname = creds['dbname']
user = creds['user']
passwd = creds['passwd']

conn_string = f"host='{host}' dbname='{dbname}' user='{user}' password='{passwd}'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
