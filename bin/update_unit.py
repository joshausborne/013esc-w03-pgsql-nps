#!/usr/bin/env python3

from config import *

def update_unit(unit):
    unit_query = (('SELECT id, name, url, flyto_lat, flyto_long, flyto_heading, flyto_range, flyto_tilt '
                   f'FROM units WHERE id = \'{unit}\''))
    cursor.execute(unit_query)
    records = cursor.fetchall()
    id,name,url,flyto_lat,flyto_long,flyto_heading,flyto_range,flyto_tilt = records[0]
    print(f'{id} {name} {url} {flyto_lat} {flyto_long} {flyto_heading} {flyto_range} {flyto_tilt}')

# Start
def main():
    while True:
        print(f"""\n\nMain Menu

        Select a unit to update:
        1. Arches National Park
        2. Bryce Canyon National Park
        3. Canyonlands National Park
        4. Capital Reef National Park
        5. Zion National Park

        Press any other key to quit\n""")
        select_unit = input(str("Pick a National Park: "))
        if select_unit == "1":
            update_unit('arch')
        elif select_unit == "2":
            update_unit('brca')
        elif select_unit == "3":
            update_unit('cany')
        elif select_unit == "4":
            update_unit('care')
        elif select_unit == "5":
            update_unit('zion')
        else:
            break

if __name__ == "__main__":
    main()

