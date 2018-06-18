import csv
import json
import datetime
import pandas as pd

now = datetime.datetime.now()
percent_year_complete = (now.timetuple().tm_yday / 365)

boundary_list = []
years_found = []
buildings_data = []

buildings_csv=pd.read_csv('data/buildings_data/bk_buildings_by_neighborhood_totals.csv', sep=',',header=None)  
for total in buildings_csv.values:
  buildings_data.append(total[1])

buildings_data.pop(0)

def create_or_append_to_boundary_list(violation, boundary_key, date_key):
  if boundary_key in violation["properties"]:
    match = next((boundary for boundary in boundary_list if boundary[boundary_key] == str(violation["properties"][boundary_key])), False)
    
  if match == False:
    create_boundary_entry(violation, boundary_key, date_key)
  else:
    print("    Found match " + str(match[boundary_key]))
    if violation["properties"][date_key][:4] in match["violations"]:
      match["violations"][violation["properties"][date_key][:4]].append(violation)
      print("  * adding violation to " + violation["properties"][date_key][:4])
    else:
      create_date_key(violation, match, date_key)


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

def generate_year_headers():
  total_years = []
  average_years = []
  violations_per_bldg = []

  for year in years_found:
    total_years.append(year + " total")
    average_years.append(year + " avg/month")
    violations_per_bldg.append(year + " violation per bldg")
  return total_years + average_years + ["buildings"] + violations_per_bldg

def generate_row(boundary, boundary_key, boundary_index):
  row = []
  total_violation_by_year = []
  average_violation_per_month = []
  violations_per_building = []
  for index, year in enumerate(years_found):
    total_violation_by_year.append(str(len(boundary["violations"][year])))
    average_violation_per_month.append(calculate_average_for_year(boundary["violations"][year], year))
    violations_per_building.append(calculate_violations_per_building(len(boundary["violations"][year]), buildings_data[boundary_index], year))
  return [boundary[boundary_key]] + total_violation_by_year + average_violation_per_month + [buildings_data[index]] + violations_per_building

def calculate_average_for_year(violations, year):
  if int(now.year) == int(year):
    return round((len(violations) / percent_year_complete) / 12, 2)
  else:
    return round(len(violations) / 12, 2)

def calculate_violations_per_building(violationNum, buildingNum, year):
  if int(now.year) == int(year):
    return round((violationNum / percent_year_complete) / float(buildingNum), 2)
  else:
    return round(float(violationNum) / float(buildingNum), 2)

def write_csv(dest_file, boundary_key):

  def sort_by_key(obj):
    return obj[boundary_key]

  with open(dest_file + '.csv', 'w') as outcsv:
    print("writing to CSV")
    writer = csv.writer(outcsv)
    writer.writerow([boundary_key] + generate_year_headers())
    for index, boundary in enumerate(sorted(boundary_list, key=sort_by_key)):
      writer.writerow(generate_row(boundary, boundary_key, index))

def process_data(source_file, dest_file, boundary_key, date_key):
  with open(source_file) as violations_data:
    violations_json = json.load(violations_data)
    print("Data loaded")
    process_count = 0
    for violation in violations_json["features"]:
      print(str(process_count) + "/" + str(len(violations_json["features"])))
      create_or_append_to_boundary_list(violation, boundary_key, date_key)
      process_count += 1

  write_csv(dest_file, boundary_key)

process_data("data/violations_data/bk_nyc_dob_violation_data.json", "data/violations_data/bk_neighborhood_violations_by_year", "neighborhood", "issue_date")

