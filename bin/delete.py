#!/usr/bin/env python3

from config import *

def delete_unit(unit):
    """
    This function deletes the 'derp' unit that is created in the 'insert' function.
    """
    delete_query = f'DELETE FROM units WHERE id = \'{unit}\''
    cursor.execute(delete_query)
    print(f"Deleted {unit}")
    conn.commit()

delete_unit('derp')

cursor.close()
