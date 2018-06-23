import json

neighborhoods_table = 'neighborhoods'

def seed_neighborhoods(c, neighborhood_json):
  print("Seeding Neighborhoods...")
  neigh_col1 = 'name'
  neigh_col2 = 'geometry'
  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} TEXT, {col2} TEXT, UNIQUE({col1}))'\
          .format(tn=neighborhoods_table, col1=neigh_col1, col2=neigh_col2))

  

  for index, neighborhood in enumerate(neighborhood_json["features"]):
    print("Neighborhood: " + str(index) + "/" + str(len(neighborhood_json["features"])))
    name = neighborhood["properties"]["neighborhood"]
    geo = json.dumps(neighborhood["geometry"], separators=(',',':'))
    
    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}) VALUES (\'{name}\', \'{geo}\')'\
      .format(tn=neighborhoods_table, col1=neigh_col1, col2=neigh_col2, name=name, geo=geo))