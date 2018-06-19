import json
import csv 
import pandas as pd

from csv_generators import bk_violation_per_building_by_census_tract

def read_csv(source):
  return pd.read_csv(source, sep=',',header=1)

def read_json(source):
  with open(source) as tract_data:
    return json.load(tract_data)

def write_csv_violations_per_building_per_year():
  buildings_data = []

  with open("data/buildings_data/csv/bk_buildings_by_census_tract_totals.csv") as buildings_csv:
    csv_reader = csv.reader(buildings_csv, delimiter=',')
    for row in csv_reader:
      buildings_data.append(row)

  violations_json = read_json("data/violations_data/json/bk_nyc_dob_violation_data.json")
  # 2010...2017
  # total
  boundary_list = []
  process_count = 0
  year_data = ["2011", "2012", "2013", "2014", "2015", "2016", "2017"]

  def create_or_append_to_boundary_list(violation):
    if "CT2010" in violation["properties"]:
      match = next((boundary for boundary in boundary_list if boundary["CT2010"] == str(violation["properties"]["CT2010"])), False)
      
      if match == False:
        create_boundary_entry(violation)
      else:
        print("    Found match " + str(match["CT2010"]))
        if violation["properties"]["issue_date"][:4] in match["violations"]:
          match["violations"][violation["properties"]["issue_date"][:4]].append(violation)
          print("  * adding violation to " + violation["properties"]["issue_date"][:4])
        else:
          create_date_key(violation, match)


  def create_boundary_entry(violation):
    print("  Boundary " + str(violation["properties"]["CT2010"]) + " created")
    new_entry = {
      "CT2010": violation["properties"]["CT2010"],
      "violations": {
        violation["properties"]["issue_date"][:4]: [violation]
      }
    }

    boundary_list.append(new_entry)

  def create_date_key(violation, match):
    match["violations"][violation["properties"]["issue_date"][:4]] = [violation]
    print("  * adding violation to " + violation["properties"]["issue_date"][:4])

  for violation in violations_json["features"]:
    print(str(process_count) + "/" + str(len(violations_json["features"])))
    create_or_append_to_boundary_list(violation)
    process_count += 1

  bk_violation_per_building_by_census_tract.generate_csv(boundary_list, year_data, buildings_data)


def write_csv_building_sales_per_year():
  # 2010...2017
  # total
  return