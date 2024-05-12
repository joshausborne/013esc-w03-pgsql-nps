# Overview

This set of scripts works with some basic US National Park Service (NPS) data. It assumes that there is already NPS data in the database. I will likely include a database dump along with the final code.

The main reason for writing the software was to create the make_unit.py script. This script will create a set of KML files for viewing NPS units in Google Earth. You can either run the script and specify a unit, or you can use it to generate all unit files at one time.


Video link can be found in the course Slack channel.


# Relational Database

I am using PostgreSQL running on Ubuntu.

The tables that are used in this app are as follows:

     Table "public.units"
     Column      |          Type          | Nullable 
-----------------+------------------------+----------
 id              | character(4)           | not null 
 name            | character varying(100) |          
 url             | character varying(250) |           
 flyto_lat       | numeric                |           
 flyto_long      | numeric                |           
 flyto_range     | numeric                |           
 flyto_tilt      | numeric                |           
 flyto_heading   | numeric                |           
 boundary_coords | text                   |           
Indexes:
    "units_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "units_x_unit_types" CONSTRAINT "fk_unit" FOREIGN KEY (unit_id) REFERENCES units(id)
    TABLE "units_x_locations" CONSTRAINT "units_x_locations_unit_id_fkey" FOREIGN KEY (unit_id) REFERENCES units(id)
    TABLE "units_x_regions" CONSTRAINT "units_x_regions_unit_id_fkey" FOREIGN KEY (unit_id) REFERENCES units(id)


The "id" field is a four character code that is assigned as the canonical "unit id" for all US National Park Service units. For example:
- arch = Arches
- brca = Bryce Canyon
- yell = Yellowstone
- yose = Yosemite

The "url" field is the URL for the official NPS website for the unit.

The "flyto" fields are some values that are used for viewing the unit in Google Earth. The include latitude and longitude, and my favorite vantage point for viewing the unit in Google Earth. These come into play when creating the "flyto" KML file.

The "boundary_coords" field is used when creating the "boundary" KML file.


     Table "public.units_x_locations"
   Column    |     Type     | Nullable |
-------------+--------------+-----------
 unit_id     | character(4) | not null |
 location_id | character(2) | not null |
Indexes:
    "units_x_locations_pkey" PRIMARY KEY, btree (unit_id, location_id)
Foreign-key constraints:
    "units_x_locations_location_id_fkey" FOREIGN KEY (location_id) REFERENCES locations(id)
    "units_x_locations_unit_id_fkey" FOREIGN KEY (unit_id) REFERENCES units(id)


The locations_id is a 2 character code that consists solely of the abbreviation for the various US states (and territories). As some Park Service units exist in multiple states, I could not include a state or location field in the main "units" table.


# Development Environment

I used vim, SSH, and psql during the development of the software.

I used Python and psycopg2 for the scripts.


# Useful Websites

- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/postgresql-python/update/)

# Future Work

- Create a menu-based nagivation through which I could select a unit for updating, then upate the field, then save.
- Give tkinter a second try. I think that I'd like to see this in a GUI, simply because I've never written a GUI app before.
