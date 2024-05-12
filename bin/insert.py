#!/usr/bin/env python3

from config import *

# this dictionary item is for the 'derp' unit, which actualy just points to my own house in Virginia
unit_list = {
        'derp': {'name':'Derpy Derp','url':'https://ausborne.net','flyto_lat':'37.6348886','flyto_long':'-77.3249311','flyto_heading':'-72','flyto_range':'125','flyto_tilt':'21'}
}

def insert_unit():
    """
    This function inserts the 'derp' unit using the 'unit_list' dictionary
    """
    for unit_id, unit_info in unit_list.items():
        insert_query = f'INSERT INTO units (id,name,url,flyto_lat,flyto_long,flyto_heading,flyto_range,flyto_tilt) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(insert_query, (unit_id, unit_info['name'], unit_info['url'], unit_info['flyto_lat'], unit_info['flyto_long'], unit_info['flyto_heading'], unit_info['flyto_range'], unit_info['flyto_tilt']))
        print(f"Inserted item {unit_id}")
        conn.commit()

insert_unit()

cursor.close()
