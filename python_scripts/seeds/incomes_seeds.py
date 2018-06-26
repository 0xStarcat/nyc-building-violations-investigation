import math
import census_tracts_seeds

incomes_table = 'incomes'

def find_tract_match(c, income):
  c.execute('SELECT * FROM {tn} WHERE {cn}=\'{ct_number}\''\
      .format(tn=census_tracts_seeds.census_tracts_table, cn="CT2010", ct_number=str(income[0][5:])))
  result = c.fetchone()
  if result:
      return result[0]
  else:
    print("  - No tract match found")
    return None

def seed_incomes(c, income_csv):
  print("Seeding incomes")
  income_col1 = 'census_tract_id'
  income_col2 = 'median_income_2011'
  income_col3 = 'median_income_2017'
  income_col4 = 'median_income_change_2011_2017'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {ct_table}(id), {col2} REAL, {col3} REAL, {col4} REAL)'\
    .format(tn=incomes_table, col1=income_col1, col2=income_col2, col3=income_col3, col4=income_col4, ct_table=census_tracts_seeds.census_tracts_table))

  for index, row in enumerate(income_csv):
    print("income: " + str(index) + "/" + str(len(income_csv)))
    ct_id = find_tract_match(c, row)
    if ct_id == None:
      continue

    mi_2011 = round(float(row[1]), 2)
    mi_2017 = round(float(row[2]), 2)
    if math.isnan(mi_2011) or math.isnan(mi_2017):
      continue

    change_2011_2017 = round(mi_2017 - mi_2011, 2)

    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}) VALUES ({ct_id}, {mi_2011}, {mi_2017}, {change_2011_2017})'\
      .format(tn=incomes_table, col1=income_col1, col2=income_col2, col3=income_col3, col4=income_col4, ct_id=ct_id, mi_2011=mi_2011, mi_2017=mi_2017, change_2011_2017=change_2011_2017))