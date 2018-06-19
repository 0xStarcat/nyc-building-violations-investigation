import csv
from helpers import violations_helpers

def generate_year_headers(years_found):
  total_years = []
  average_years = []
  violations_per_bldg = []

  for year in sorted(years_found):
    total_years.append(year + " total")
    average_years.append(year + " avg/month")
    violations_per_bldg.append(year + " violation per bldg")
  return total_years + average_years + ["buildings"] + violations_per_bldg

def generate_row(boundary, years_found, buildings_data):
  row = []
  total_violation_by_year = []
  average_violation_per_month = []
  violations_per_building = []
  for year in sorted(years_found):
    total_violation_by_year.append(str(len(boundary["violations"][year]))) if year in boundary["violations"] else total_violation_by_year.append("0")
    average_violation_per_month.append(violations_helpers.calculate_average_for_year(boundary["violations"][year], year)) if year in boundary["violations"] else average_violation_per_month.append("0")
    violations_per_building.append(violations_helpers.calculate_violations_per_building(len(boundary["violations"][year]), violations_helpers.match_boundary_to_building_num(boundary, "CT2010", buildings_data), year)) if year in boundary["violations"] else violations_per_building.append("0")

  return [boundary["CT2010"]] + total_violation_by_year + average_violation_per_month + [violations_helpers.match_boundary_to_building_num(boundary, "CT2010", buildings_data)] + violations_per_building

def write_csv(boundary_list, years_found, buildings_data):
  with open("data/violations_data/csv/bk_census_tract_violations_by_year.csv", 'w') as outcsv:
    print("writing to CSV")
    writer = csv.writer(outcsv)
    writer.writerow(["CT2010"] + generate_year_headers(years_found))
    
    for boundary in sorted(boundary_list, key=lambda obj: obj["CT2010"]):
      if boundary["CT2010"] != "" and "CT2010" in boundary:
        writer.writerow(generate_row(boundary, years_found, buildings_data))