import sqlite3
import json

import neighborhoods_seeds
import census_tracts_seeds
import buildings_seeds
import violations_seeds

sqlite_file = 'bk_building_violation_project.sqlite'

census_tracts_table = 'census_tracts'
residential_buildings_table = 'residential_buildings_table'
violations_table = 'violations_table'
sales_table = 'sales_table'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('pragma foreign_keys=on;')


def drop_tables():
  c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=violations_seeds.violations_table))
  c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=buildings_seeds.buildings_table))
  c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=census_tracts_seeds.census_tracts_table))
  c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=neighborhoods_seeds.neighborhoods_table))

# drop_tables()

# neighborhood_json = json.load(open('data/boundary_data/geojson/bk_neighborhoods.geojson'))
# building_json = json.load(open('data/buildings_data/processed_mappluto.geojson'))
violations_json = json.load(open('data/violations_data/bk_violation_data_2008_2017.json'))

# neighborhoods_seeds.seed_neighborhoods(c, neighborhood_json)
# census_tracts_seeds.seed_census_tracts(c, neighborhood_json)
# buildings_seeds.seed_buildings(c, building_json) # Takes about half an hour due ot foriegn key indexing by geodata
violations_seeds.seed_violations(c, violations_json)
print("Seeding complete.")

# Test the DB
# c.execute('SELECT census_tracts_table.* FROM census_tracts_table INNER JOIN neighborhoods_table ON census_tracts_table.neighborhood_id = neighborhoods_table.id WHERE neighborhoods_table.name = \'Williamsburg\'')
# all_rows = c.fetchall()
# print(all_rows)

c.execute('SELECT * FROM violations')
all_rows = c.fetchall()
print(all_rows[0])


conn.commit()
conn.close()