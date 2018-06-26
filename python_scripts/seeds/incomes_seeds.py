import math
import census_tracts_seeds
import neighborhoods_seeds

incomes_table = 'incomes'

def find_tract_and_neighborhood_match(c, income):
  c.execute('SELECT * FROM {tn} WHERE {cn}=\'{ct_number}\''\
      .format(tn=census_tracts_seeds.census_tracts_table, cn="CT2010", ct_number=str(income[0][5:])))
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

def seed_incomes(c, income_csv):
  print("Seeding incomes")
  income_col1 = 'census_tract_id'
  income_col2 = 'neighborhood_id'
  income_col3 = 'median_income_2011'
  income_col4 = 'median_income_2017'
  income_col5 = 'median_income_change_2011_2017'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {ct_table}(id), {col2} INTEGER NOT NULL REFERENCES {n_table}(id), {col3} REAL, {col4} REAL, {col5} REAL)'\
    .format(tn=incomes_table, col1=income_col1, col2=income_col2, col3=income_col3, col4=income_col4, col5=income_col5, ct_table=census_tracts_seeds.census_tracts_table, n_table=neighborhoods_seeds.neighborhoods_table))

  for index, row in enumerate(income_csv):
    print("income: " + str(index) + "/" + str(len(income_csv)))
    foreign_keys = find_tract_and_neighborhood_match(c, row)
    if foreign_keys == None:
      continue

    ct_id = foreign_keys["census_tract_id"]
    n_id = foreign_keys["neighborhood_id"]

    mi_2011 = round(float(row[1]), 2)
    mi_2017 = round(float(row[2]), 2)
    if math.isnan(mi_2011) or math.isnan(mi_2017):
      continue

    change_2011_2017 = round(mi_2017 - mi_2011, 2)

    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}, {col5}) VALUES ({ct_id}, {n_id}, {mi_2011}, {mi_2017}, {change_2011_2017})'\
      .format(tn=incomes_table, col1=income_col1, col2=income_col2, col3=income_col3, col4=income_col4, col5=income_col5, ct_id=ct_id, n_id=n_id, mi_2011=mi_2011, mi_2017=mi_2017, change_2011_2017=change_2011_2017))
