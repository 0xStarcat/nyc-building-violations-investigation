import math
import census_tracts_seeds
import neighborhoods_seeds

rents_table = 'rents'

def find_tract_and_neighborhood_match(c, rent):
  if rent[2][:5] != "36047":
    print(" - Not Brooklyn CT 36047 - skipping")
    return None

  c.execute('SELECT * FROM {tn} WHERE {cn}=\'{ct_number}\''\
      .format(tn=census_tracts_seeds.census_tracts_table, cn="CT2010", ct_number=str(rent[2][5:])))
  
  result = c.fetchone()
  if result:
    return {
      "census_tract_id": result[0],
      "neighborhood_id": get_neighborhood_id(c, result)[0]
      }
  else:
    print("  - No tract match found")
    return None

def get_neighborhood_id(c, tract):
  c.execute('SELECT * FROM {tn} WHERE {cn}={n_id}'\
    .format(tn=neighborhoods_seeds.neighborhoods_table, cn='id', n_id=tract[1]))
  return c.fetchone()

def seed_rents(c, rent_csv):
  print("Seeding rents")
  rent_col1 = 'census_tract_id'
  rent_col2 = 'neighborhood_id'
  rent_col3 = 'median_rent_2011'
  rent_col4 = 'median_rent_2017'
  rent_col5 = 'median_rent_change_2011_2017'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {ct_table}(id), {col2} INTEGER NOT NULL REFERENCES {n_table}(id), {col3} REAL, {col4} REAL, {col5} REAL)'\
    .format(tn=rents_table, col1=rent_col1, col2=rent_col2, col3=rent_col3, col4=rent_col4, col5=rent_col5, ct_table=census_tracts_seeds.census_tracts_table, n_table=neighborhoods_seeds.neighborhoods_table))

  for index, row in enumerate(rent_csv):
    print("rent: " + str(index) + "/" + str(len(rent_csv)))
    
    foreign_keys = find_tract_and_neighborhood_match(c, row)
    if foreign_keys == None:
      continue

    if not row[3] or not row[4]:
      continue

    ct_id = foreign_keys["census_tract_id"]
    n_id = foreign_keys["neighborhood_id"]
        
    mr_2011 = round(float(row[3]), 2)
    mr_2017 = round(float(row[4]), 2)

    change_2011_2017 = round(mr_2017 - mr_2011, 2)

    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}, {col5}) VALUES ({ct_id}, {n_id}, {n_id}{mr_2011}, {mr_2017}, {change_2011_2017})'\
      .format(tn=rents_table, col1=rent_col1, col2=rent_col2, col3=rent_col3, col4=rent_col4, col5=rent_col5, ct_id=ct_id, n_id=n_id, mr_2011=mr_2011, mr_2017=mr_2017, change_2011_2017=change_2011_2017))