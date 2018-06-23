import json
import boundary_helpers

neighborhoods_table = 'neighborhoods'
census_tracts_table = 'census_tracts'

def match_neighborhood_name_to_id(c, name):
    c.execute('SELECT * FROM {tn} WHERE {cn}=\'{neighorhood_name}\''\
      .format(tn=neighborhoods_table, cn="name", neighorhood_name=name))
    result = c.fetchone()
    if result:
      return result[0]
    else:
      # print("  - No neighborhood match found")
      return None

def seed_census_tracts(c, neighborhood_json):
  print("Seeding Census Tracts...")
  ct_col1 = 'neighborhood_id'
  ct_col2 = 'name'
  ct_col3 = 'CTLabel'
  ct_col4 = 'CT2010'
  ct_col5 = 'geometry'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {ref_table}(id), {col2} TEXT, {col3} TEXT, {col4} TEXT, {col5} TEXT, UNIQUE({col2}))'\
    .format(tn=census_tracts_table, ref_table=neighborhoods_table, col1=ct_col1, col2=ct_col2, col3=ct_col3, col4=ct_col4, col5=ct_col5))

  census_tract_json = json.load(open('data/boundary_data/geojson/bk_census_tracts_2010.geojson'))

  for index, ct in enumerate(census_tract_json["features"]):
    print("CT: " + str(index) + "/" + str(len(census_tract_json["features"])))
    neighborhood_id = match_neighborhood_name_to_id(c, boundary_helpers.get_neighborhood_name_from_coordinates(ct["geometry"], neighborhood_json))
    if neighborhood_id == None:
      continue
    name = ct["properties"]["CT2010"]
    ct_label = ct["properties"]["CTLabel"]
    ct_2010 = ct["properties"]["CT2010"]
    geometry = json.dumps(ct["geometry"], separators=(',', ':'))


    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}, {col5}) VALUES ({neighborhood_id}, \'{name}\', \'{ct_label}\', \'{ct_2010}\', \'{geometry}\')'\
      .format(tn=census_tracts_table, col1=ct_col1, col2=ct_col2, col3=ct_col3, col4=ct_col4, col5=ct_col5, neighborhood_id=neighborhood_id, name=name, ct_label=ct_label, ct_2010=ct_2010, geometry=geometry))