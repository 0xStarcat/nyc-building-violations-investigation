import sqlite3
import json
import csv

import neighborhoods_seeds
import census_tracts_seeds
import buildings_seeds
import violations_seeds
import incomes_seeds
import rents_seeds
import sales_seeds
import permits_seeds

sqlite_file = 'bk_building_violation_project.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('pragma foreign_keys=on;')


def drop_tables():
  c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=permits_seeds.permits_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=sales_seeds.sales_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=rents_seeds.rents_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=incomes_seeds.incomes_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=violations_seeds.violations_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=buildings_seeds.buildings_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=census_tracts_seeds.census_tracts_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=neighborhoods_seeds.neighborhoods_table))

# drop_tables()

# neighborhood_json = json.load(open('data/boundary_data/geojson/bk_neighborhoods.geojson'))
# building_json = json.load(open('data/buildings_data/processed_mappluto.geojson'))
# violations_json = json.load(open('data/violations_data/bk_violation_data_2008_2017.json'))
# incomes_csv = list(csv.reader(open("data/demographic_data/bk_median_income_2017.csv")))[1:]
# rents_csv = list(csv.reader(open("data/rent_data/censustract-medianrentall2017.csv")))[1:]
# sales_csv = list(csv.reader(open("data/sales_data/bk_property_sales_2011_2017.csv")))[1:]
# permits_csv = list(csv.reader(open("data/permit_data/processed_bk_permit_data_2011_2017.csv")))[1:]



# neighborhoods_seeds.seed_neighborhoods(c, neighborhood_json)
# census_tracts_seeds.seed_census_tracts(c, neighborhood_json)
# buildings_seeds.seed_buildings(c, building_json) # Takes about half an hour due ot foriegn key indexing by geodata
# violations_seeds.seed_violations(c, violations_json)
# incomes_seeds.seed_incomes(c, incomes_csv)
# rents_seeds.seed_rents(c, rents_csv)
# sales_seeds.seed_sales(c, sales_csv)
# permits_seeds.seed_permits(c, permits_csv)

print("Seeding complete.")

# Test DB
c.execute('SELECT * FROM permits')
all_rows = c.fetchall()
print(all_rows[:30])


conn.commit()
conn.close()