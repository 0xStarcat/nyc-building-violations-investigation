import sqlite3
import json
import boundary_helpers

sqlite_file = 'bk_building_violation_project.sqlite'
neighborhoods_table = 'neighborhoods_table'
census_tracts_table = 'census_tracts_table'
residential_buildings_table = 'residential_buildings_table'
violations_table = 'violations_table'
sales_table = 'sales_table'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('pragma foreign_keys=on;')

neighborhood_json = json.load(open('data/boundary_data/geojson/bk_neighborhoods.geojson'))

def seed_neighborhoods(neighborhood_json):
  # Seed Neighborhoods from geojson
  neigh_col1 = 'name'
  neigh_col2 = 'geometry'
  c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=neighborhoods_table))
  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} TEXT, {col2} TEXT, UNIQUE({col1}))'\
          .format(tn=neighborhoods_table, col1=neigh_col1, col2=neigh_col2))

  

  for neighborhood in neighborhood_json["features"]:
    name = neighborhood["properties"]["neighborhood"]
    geo = json.dumps(neighborhood["geometry"], separators=(',',':'))
    
    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}) VALUES (\'{name}\', \'{geo}\')'\
      .format(tn=neighborhoods_table, col1=neigh_col1, col2=neigh_col2, name=name, geo=geo))


def seed_census_tracts(neighborhood_json):
  # seed Census Tracts from geojson
  ct_col1 = 'neighborhood_id'
  ct_col2 = 'name'
  ct_col3 = 'CTLabel'
  ct_col4 = 'CT2010'
  ct_col5 = 'geometry'

  c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=census_tracts_table))
  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {ref_table}(id), {col2} TEXT, {col3} TEXT, {col4} TEXT, {col5} TEXT, UNIQUE({col2}))'\
    .format(tn=census_tracts_table, ref_table=neighborhoods_table, col1=ct_col1, col2=ct_col2, col3=ct_col3, col4=ct_col4, col5=ct_col5))

  def match_neighborhood_name_to_id(name):
    c.execute('SELECT * FROM {tn} WHERE {cn}=\'{neighorhood_name}\''\
      .format(tn=neighborhoods_table, cn="name", neighorhood_name=name))
    print(name)
    result = c.fetchone()
    if result:
      return result[0]
    else:
      print("No result found")
      return None

  census_tract_json = json.load(open('data/boundary_data/geojson/bk_census_tracts_2010.geojson'))

  for index, ct in enumerate(census_tract_json["features"]):
    print("CT: " + str(index) + "/" + str(len(census_tract_json["features"])))
    neighborhood_id = match_neighborhood_name_to_id(boundary_helpers.get_neighborhood_name_from_coordinates(ct["geometry"], neighborhood_json))
    if neighborhood_id == None:
      continue
    name = ct["properties"]["CT2010"]
    ct_label = ct["properties"]["CTLabel"]
    ct_2010 = ct["properties"]["CT2010"]
    geometry = json.dumps(ct["geometry"], separators=(',', ':'))


    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}, {col5}) VALUES ({neighborhood_id}, \'{name}\', \'{ct_label}\', \'{ct_2010}\', \'{geometry}\')'\
      .format(tn=census_tracts_table, col1=ct_col1, col2=ct_col2, col3=ct_col3, col4=ct_col4, col5=ct_col5, neighborhood_id=neighborhood_id, name=name, ct_label=ct_label, ct_2010=ct_2010, geometry=geometry))

# seed_neighborhoods(neighborhood_json)
# seed_census_tracts(neighborhood_json)

c.execute('SELECT census_tracts_table.* FROM census_tracts_table INNER JOIN neighborhoods_table ON census_tracts_table.neighborhood_id = neighborhoods_table.id WHERE neighborhoods_table.name = \'Williamsburg\'')
all_rows = c.fetchall()
print(all_rows)



conn.commit()
conn.close()