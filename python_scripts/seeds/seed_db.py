import sqlite3
import json
import csv

import neighborhoods_seeds
import census_tracts_seeds
import buildings_seeds
import violations_seeds
import incomes_seeds
import rents_seeds
import racial_makeup_seeds
import sales_seeds
import permits_seeds
import service_calls_seeds
import building_events_seeds

sqlite_file = 'bk_building_violation_project.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('pragma foreign_keys=on;')


def drop_tables():
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=building_events_seeds.building_events_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=service_calls_seeds.service_calls_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=permits_seeds.permits_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=sales_seeds.sales_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=violations_seeds.violations_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=buildings_seeds.buildings_table))
  c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=racial_makeup_seeds.racial_makeup_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=rents_seeds.rents_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=incomes_seeds.incomes_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=census_tracts_seeds.census_tracts_table))
  # c.execute('DROP TABLE IF EXISTS {tn}'.format(tn=neighborhoods_seeds.neighborhoods_table))

# drop_tables()

# neighborhood_json = json.load(open('data/boundary_data/geojson/bk_neighborhoods.geojson'))
# incomes_csv = list(csv.reader(open("data/income_data/bk_median_income_2017.csv")))[1:]
# rents_csv = list(csv.reader(open("data/rent_data/censustract-medianrentall2017.csv")))[1:]
# building_json = json.load(open('data/buildings_data/processed_mappluto.geojson'))
# violations_json = json.load(open('data/violations_data/bk_violation_data_2008_2017.json'))
# racial_makeup_csv = list(csv.reader(open("data/race_data/sub-borougharea-percentwhite.csv")))[1:]
# sales_csv = list(csv.reader(open("data/sales_data/bk_property_sales_2011_2017.csv")))[1:]
# permits_csv = list(csv.reader(open("data/permit_data/processed_bk_permit_data_2011_2017.csv")))[1:]
# dob_service_calls_csv = list(csv.reader(open("data/service_calls/bk_dob_311_Service_Requests_from_2010_to_Present.csv")))[1:]
# hpd_service_calls_csv = list(csv.reader(open("data/service_calls/bk_hpd_311_Service_Requests_from_2010_to_Present.csv")))[1:]
# service_calls_csv = dob_service_calls_csv + hpd_service_calls_csv

# neighborhoods_seeds.seed_neighborhoods(c, neighborhood_json)
# census_tracts_seeds.seed_census_tracts(c, neighborhood_json)
# incomes_seeds.seed_incomes(c, incomes_csv)
# rents_seeds.seed_rents(c, rents_csv)
# buildings_seeds.seed_buildings(c, building_json) # Takes about half an hour due ot foriegn key indexing by geodata
# building_events_seeds.seed_building_events(c)
# violations_seeds.seed_violations(c, violations_json)
# racial_makeup_seeds.seed_racial_makeups(c, racial_makeup_csv)
# sales_seeds.seed_sales(c, sales_csv)
# permits_seeds.seed_permits(c, permits_csv)
# service_calls_seeds.seed_service_calls(c, service_calls_csv)

print("Seeding complete.")

# Test DB
c.execute('SELECT * FROM neighborhoods')
all_rows = c.fetchall()
for row in all_rows:
  print(row[1])
# print(all_rows[0])


conn.commit()
conn.close()