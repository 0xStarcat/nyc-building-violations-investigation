import sqlite3
import json

from seeds import neighborhoods_seeds
from seeds import census_tracts_seeds

sqlite_file = 'bk_building_violation_project.sqlite'

neighborhoods_table = 'neighborhoods'
census_tracts_table = 'census_tracts'
residential_buildings_table = 'residential_buildings_table'
violations_table = 'violations_table'
sales_table = 'sales_table'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('pragma foreign_keys=on;')

neighborhood_json = json.load(open('data/boundary_data/geojson/bk_neighborhoods.geojson'))

def drop_tables():
  c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=census_tracts_table))
  c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=neighborhoods_table))

# drop_tables()

# neighborhoods_seeds.seed_neighborhoods(c, neighborhood_json)
# census_tracts_seeds.seed_census_tracts(c, neighborhood_json)
print("Seeding complete.")

# Test the DB
# c.execute('SELECT census_tracts_table.* FROM census_tracts_table INNER JOIN neighborhoods_table ON census_tracts_table.neighborhood_id = neighborhoods_table.id WHERE neighborhoods_table.name = \'Williamsburg\'')
# all_rows = c.fetchall()
# print(all_rows)

c.execute('SELECT * FROM neighborhoods')
all_rows = c.fetchall()
print(all_rows[0])


conn.commit()
conn.close()