#!/usr/bin/env python3

import sys, os
from datetime import datetime
from config import *
from jinja2 import Environment, FileSystemLoader

now = datetime.now()
unit = sys.argv[1]

env = Environment(loader=FileSystemLoader(templates))

def make_everything(unit):
    global_query = (('SELECT id, name, url, boundary_coords, flyto_lat, flyto_long, flyto_heading, '
                     'flyto_range, flyto_tilt '
                     f'FROM units WHERE id = \'{unit}\''))
    cursor.execute(global_query)
    records = cursor.fetchall()
    unit,name,url,boundary_coords,lat,long,head,flyto_range,tilt = records[0]
    print('---------------------------------')
    print(f'Starting build of files for {unit}')
    # run all build functions
    make_boundary(unit,name,boundary_coords,now,placemark_img)
    make_flyto(unit,name,lat,long,head,flyto_range,tilt,now,placemark_img)

def make_boundary(unit,name,boundary_coords,now,placemark_img):
    template = env.get_template('nps-boundary-template.kml')
    boundary_outfile = (f'nps-{unit}-boundary.kml')
    boundary_outfile = os.path.join(boundaries,boundary_outfile)
    print(f'Creating boundary kml file for {unit}')
    data = {
        'unit': unit,
        'name': name,
        'boundary_coords': boundary_coords,
        'now': now,
        'placemark_img': placemark_img
    }
    output = template.render(data)
    with open(boundary_outfile,'w') as file:
        file.write(output)

def make_flyto(unit,name,lat,long,head,flyto_range,tilt,now,placemark_img):
    template = env.get_template('nps-flyto-template.kml')
    flyto_outfile = (f'nps-{unit}-flyto.kml')
    flyto_outfile = os.path.join(flytos,flyto_outfile)
    print(f'Creating flyto kml file for {unit}')
    data = {
        'unit': unit,
        'name': name,
        'lat': lat,
        'long': long,
        'head': head,
        'flyto_range': flyto_range,
        'tilt': tilt,
        'now': now,
        'placemark_img': placemark_img
    }
    output = template.render(data)
    with open(flyto_outfile,'w') as file:
        file.write(output)

if unit == 'all':
    unit_list_query = (('SELECT id FROM units ORDER BY id'))
    cursor.execute(unit_list_query)
    unit_list = cursor.fetchall()
    for unit in unit_list:
        unit = unit[0]
        make_everything(unit)
else:
    make_everything(unit)

conn.commit()
cursor.close()
