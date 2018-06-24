import json
import neighborhoods_seeds
import census_tracts_seeds

from shapely.geometry import mapping, shape, Point

buildings_table = 'buildings'

def convert_building_polygon_to_point(geometry):
  polygon = shape(geometry)
  return polygon.representative_point()

def match_point_to_neighborhood_and_census_tract_id(c, neighborhoods_data, point):
  match = next((neighborhood for neighborhood in neighborhoods_data if shape(json.loads(neighborhood[2])).contains(point)), False) 
  if match:
    c.execute('SELECT * FROM {ct_table} WHERE neighborhood_id={n_id}'.format(ct_table=census_tracts_seeds.census_tracts_table, n_id=match[0]))
    matching_tracts = c.fetchall()
    return match_point_to_census_tract_id(c, matching_tracts, point, match)
  else:
    return None

def match_point_to_census_tract_id(c, census_tracts_data, point, neighborhood_match):
  match = next((tract for tract in census_tracts_data if shape(json.loads(tract[5])).contains(point)), False) 
  if match:
    return {
      "neighborhood_id": neighborhood_match[0],
      "census_tract_id": match[0]
    }
  else:
    return None

def seed_buildings(c, building_json):
  print("Seeding Buildings...")
  bldg_col1 = 'block'
  bldg_col2 = 'lot'
  bldg_col3 = 'address'
  bldg_col4 = 'geometry'
  bldg_col5 = 'year_built'
  bldg_col6 = 'census_tract_id'
  bldg_col7 = 'neighborhood_id'

  c.execute('SELECT * FROM neighborhoods')
  data = c.fetchall()
  neighborhoods_data = data

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} TEXT, {col2} TEXT, {col3} TEXT, {col4} TEXT, {col5} INTEGER, {col6} INTEGER NOT NULL REFERENCES {ct_table}(id), {col7} INTEGER NOT NULL REFERENCES {n_table}(id), UNIQUE({col3}))'\
    .format(tn=buildings_table, col1=bldg_col1, col2=bldg_col2, col3=bldg_col3, col4=bldg_col4, col5=bldg_col5, col6=bldg_col6, col7=bldg_col7, ct_table=census_tracts_seeds.census_tracts_table, n_table=neighborhoods_seeds.neighborhoods_table))

  c.execute('CREATE INDEX idx_block_and_lot ON {tn}({col1}, {col2})'.format(tn=buildings_table, col1=bldg_col1, col2=bldg_col2))
  c.execute('CREATE UNIQUE INDEX idx_address ON {tn}({col3})'.format(tn=buildings_table, col3=bldg_col3))
  c.execute('CREATE INDEX idx_census_tract_id ON {tn}({col6})'.format(tn=buildings_table, col6=bldg_col6))
  c.execute('CREATE INDEX idx_neighborhood_id ON {tn}({col7})'.format(tn=buildings_table, col7=bldg_col7))

  for index, building in enumerate(building_json["features"]):
    print("Building: " + str(index) + "/" + str(len(building_json["features"])))
    
    if "Block" not in building["properties"] or "Lot" not in building["properties"] or "Address" not in building["properties"]:
      print("  * Missing Block, Lot, or Address")
      continue

    block = building["properties"]["Block"]
    lot = building["properties"]["Lot"]
    address = building["properties"]["Address"]
    geometry = json.dumps(building["geometry"], separators=(',',':'))
    year_built = building["properties"]["YearBuilt"]
    foreign_keys = match_point_to_neighborhood_and_census_tract_id(c, neighborhoods_data, convert_building_polygon_to_point(building["geometry"]))
    if foreign_keys == None:
      print("  * no matches found")
      continue

    neighborhood_id = foreign_keys["neighborhood_id"]
    census_tract_id = foreign_keys["census_tract_id"]


    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}, {col5}, {col6}, {col7}) VALUES (\'{block}\', \'{lot}\', \"{address}\", \'{geometry}\', {year_built}, {census_tract_id}, {neighborhood_id})'\
      .format(tn=buildings_table, col1=bldg_col1, col2=bldg_col2, col3=bldg_col3, col4=bldg_col4, col5=bldg_col5, col6=bldg_col6, col7=bldg_col7, block=block, lot=lot, address=address, geometry=geometry, year_built=year_built,census_tract_id=census_tract_id, neighborhood_id=neighborhood_id))