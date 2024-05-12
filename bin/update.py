#!/usr/bin/env python3

from config import *

unit_list = {
    'arch': {'name':'blah blah blah','url':'https://www.nps.gov/arch/index.htm','flyto_lat':'38.743728','flyto_long':'-109.499292','flyto_heading':'318','flyto_range':'720','flyto_tilt':'75'},
    'brca': {'name':'bry','url':'https://www.nps.gov/brca/index.htm','flyto_lat':'37.646095','flyto_long':'-112.137013','flyto_heading':'-38','flyto_range':'1250','flyto_tilt':'80'},
    'cany': {'name':'erksdfasdf National Park','url':'https://www.nps.gov/canysasdf/index.htm','flyto_lat':'38.376657','flyto_long':'-109.808569','flyto_heading':'105','flyto_range':'4400','flyto_tilt':'82'},
    'care': {'name':'Capitsdfasdfa National Park','url':'https://www.nps.gov/care/iasdfndex.htm','flyto_lat':'38.287537','flyto_long':'-111.234164','flyto_heading':'-94','flyto_range':'11000','flyto_tilt':'78'},
    'zion': {'name':'Zion Nsdfasdfational Park','url':'https://www.sdfasdfasdnps.gov/zion/index.htm','flyto_lat':'37.238655','flyto_long':'-112.961166','flyto_heading':'14','flyto_range':'4000','flyto_tilt':'81'}
}

def update_units():
    """
    This function breaks all five Utah National Parks by changing their values.
    """
    for unit_id, unit_info in unit_list.items():
        reset_query = f'UPDATE units SET name = %s, url = %s, flyto_lat = %s, flyto_long = %s, flyto_heading = %s, flyto_range = %s, flyto_tilt = %s WHERE id = %s'
        cursor.execute(reset_query, (unit_info['name'], unit_info['url'], unit_info['flyto_lat'], unit_info['flyto_long'], unit_info['flyto_heading'], unit_info['flyto_range'], unit_info['flyto_tilt'], unit_id))
        print(f"Updated {unit_id}")
        conn.commit()

update_units()

cursor.close()
