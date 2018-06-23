import csv
import json
import datetime
import pandas as pd
from csv_generators import bk_census_tract_violations_by_year
from csv_generators import bk_neighborhood_violations_by_year

now = datetime.datetime.now()
percent_year_complete = (now.timetuple().tm_yday / 365)

boundary_list = []
years_found = []

buildings_data = []

# Creates data files splitting all the data by boundary and year 
# includes columns for 
# Total Buildings
# 

def create_or_append_to_boundary_list(violation, boundary_key, date_key):
  if boundary_key in violation["properties"]:
    match = next((boundary for boundary in boundary_list if boundary[boundary_key] == str(violation["properties"][boundary_key])), False)
    
  if match:
    print("    Found match " + str(match[boundary_key]))
    if violation["properties"][date_key][:4] in match["violations"]:
      match["violations"][violation["properties"][date_key][:4]].append(violation)
      print("  * adding violation to " + violation["properties"][date_key][:4])
    else:
      create_date_key(violation, match, date_key)
  else:
    create_boundary_entry(violation, boundary_key, date_key)


def create_boundary_entry(violation, boundary_key, date_key):
  print("  Boundary " + str(violation["properties"][boundary_key]) + " created")
  new_entry = {
    boundary_key: violation["properties"][boundary_key],
    "violations": {
      violation["properties"][date_key][:4]: [violation]
    }
  }
  boundary_list.append(new_entry)
  push_year_found(violation["properties"][date_key][:4])

def create_date_key(violation, match, date_key):
  match["violations"][violation["properties"][date_key][:4]] = [violation]
  print("    * new violation date key " + violation["properties"][date_key][:4])
  print("  * adding violation to " + violation["properties"][date_key][:4])
  push_year_found(violation["properties"][date_key][:4])

def push_year_found(year):
  if year in years_found:
    return
  else:
    years_found.append(year)

def process_data(source_file, boundary_key, date_key):
  with open(source_file) as violations_data:
    violations_json = json.load(violations_data)
    print("Data loaded")
    process_count = 0
    for violation in violations_json["features"]:
      print(str(process_count) + "/" + str(len(violations_json["features"])))
      create_or_append_to_boundary_list(violation, boundary_key, date_key)
      process_count += 1


def process_neighborhood_data(source_file, boundary_key, date_key):
  boundary_list = []
  years_found = []
  buildings_csv=pd.read_csv('data/buildings_data/csv/bk_buildings_by_neighborhood_totals.csv', sep=',',header=None)  
  for total in buildings_csv.values:
    buildings_data.append(total)

  buildings_data.pop(0)
  process_data(source_file, boundary_key, date_key)
  bk_neighborhood_violations_by_year.write_csv(boundary_list, years_found, buildings_data)

def process_census_tract_data(source_file, boundary_key, date_key):
  boundary_list = []
  years_found = []
  buildings_csv=pd.read_csv('data/buildings_data/csv/bk_buildings_by_census_tract_totals.csv', sep=',',header=None)  
  for total in buildings_csv.values:
    buildings_data.append(total)

  buildings_data.pop(0)
  process_data(source_file, boundary_key, date_key)
  bk_census_tract_violations_by_year.write_csv(boundary_list, years_found, buildings_data)

# process_neighborhood_data("data/violations_data/json/processed_bk_violation_data_2011_2017.json", "neighborhood", "issue_date")

process_census_tract_data("data/violations_data/json/processed_bk_violation_data_2011_2017.json", "CT2010", "issue_date")

