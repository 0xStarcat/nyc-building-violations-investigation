import sqlite3
import json


sqlite_file = 'bk_building_violation_project.sqlite'
neighborhoods_table = 'neighborhoods_table'
census_tracts_table = 'census_tracts_table'
residential_buildings_table = 'residential_buildings_table'
violations_table = 'violations_table'
sales_table = 'sales_table'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# Seed Neighborhoods from geojson
c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=neighborhoods_table))
c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, geometry TEXT, UNIQUE(name))'\
        .format(tn=neighborhoods_table))

neighborhood_json = json.load(open('data/boundary_data/geojson/bk_neighborhoods.geojson'))

for neighborhood in neighborhood_json["features"]:
  name = neighborhood["properties"]["neighborhood"]
  geo = json.dumps(neighborhood["geometry"], separators=(',',':'))
  c.execute('INSERT OR IGNORE INTO {tn} (name, geometry) VALUES (\'{name}\', \'{geo}\')'\
    .format(tn=neighborhoods_table, name=name, geo=geo))


c.execute('SELECT * FROM {tn} WHERE {cn}="Bay Ridge"'.\
        format(tn=neighborhoods_table, cn="name"))

all_rows = c.fetchall()
print(all_rows)



conn.commit()
conn.close()