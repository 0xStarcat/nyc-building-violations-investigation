import math
import census_tracts_seeds

rents_table = 'rents'

def find_tract_match(c, rent):
  if rent[2][:5] != "36047":
    print(" - Not Brooklyn CT 36047 - skipping")
    return None

  c.execute('SELECT * FROM {tn} WHERE {cn}=\'{ct_number}\''\
      .format(tn=census_tracts_seeds.census_tracts_table, cn="CT2010", ct_number=str(rent[2][5:])))
  
  result = c.fetchone()
  if result:
      return result[0]
  else:
    print("  - No tract match found")
    return None

def seed_rents(c, rent_csv):
  print("Seeding rents")
  rent_col1 = 'census_tract_id'
  rent_col2 = 'median_rent_2011'
  rent_col3 = 'median_rent_2017'
  rent_col4 = 'median_rent_change_2011_2017'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {ct_table}(id), {col2} REAL, {col3} REAL, {col4} REAL)'\
    .format(tn=rents_table, col1=rent_col1, col2=rent_col2, col3=rent_col3, col4=rent_col4, ct_table=census_tracts_seeds.census_tracts_table))

  for index, row in enumerate(rent_csv):
    print("rent: " + str(index) + "/" + str(len(rent_csv)))
    ct_id = find_tract_match(c, row)
    if ct_id == None:
      continue
    if not row[3] or not row[4]:
      continue
      
    mr_2011 = round(float(row[3]), 2)
    mr_2017 = round(float(row[4]), 2)

    change_2011_2017 = round(mr_2017 - mr_2011, 2)

    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}) VALUES ({ct_id}, {mr_2011}, {mr_2017}, {change_2011_2017})'\
      .format(tn=rents_table, col1=rent_col1, col2=rent_col2, col3=rent_col3, col4=rent_col4, ct_id=ct_id, mr_2011=mr_2011, mr_2017=mr_2017, change_2011_2017=change_2011_2017))