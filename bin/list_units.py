#!/usr/bin/env python3

import sys
from config import *

# check to see if an argument is being passed into the script
if len(sys.argv) < 2:
    print("Script requires a state abbreviation to be specified as an argument")
    sys.exit(1)
else:
    state = sys.argv[1]

def list_units_by_state(state):
    """
    This function selects the names of all National Parks that are located within a given state
    """
    select_query = (('SELECT id, name '
                     'FROM units '
                     'INNER JOIN units_x_locations ON units.id = units_x_locations.unit_id '
                     f'WHERE units_x_locations.location_id = \'{state}\' '
                     'AND units.name like \'%National Park\' '
                     'ORDER BY name'))
    cursor.execute(select_query)
    unit_list = cursor.fetchall()
    for unit,name in unit_list:
        print(name)

list_units_by_state(state)

cursor.close()
