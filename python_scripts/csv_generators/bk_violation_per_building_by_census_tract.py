import csv
from helpers import violations_helpers

def generate_row(boundary, year_data, buildings_data):
  violations_per_building = []
  for year in sorted(year_data):
    total_buildings = violations_helpers.match_boundary_to_building_num(boundary, "CT2010", buildings_data)
    violations_per_building.append(violations_helpers.calculate_violations_per_building(len(boundary["violations"][year]), total_buildings, year)) if year in boundary["violations"] else violations_per_building.append("0")

  average_violations_total = violations_helpers.calculate_average_violations_total(violations_per_building, year_data)
  average_buildings_per_violation = round(float(total_buildings) / (1.0 / float(average_violations_total))) if average_violations_total != 0 else 0

  return [boundary["CT2010"]] + violations_per_building + [average_violations_total, average_buildings_per_violation]

def generate_csv(boundary_list, year_data, buildings_data):
  with open('data/violations_data/csv/bk_violation_per_building_by_census_tract.csv', 'w') as outcsv:
    print("writing to CSV")
    writer = csv.writer(outcsv)
    writer.writerow(["CT2010"] + year_data + ["Avg 2011-2017", "Avg Num Bldgs per Violation"])
    for boundary in sorted(boundary_list, key=lambda obj: obj["CT2010"]):
      if boundary["CT2010"] != "" and "CT2010" in boundary:
        writer.writerow(generate_row(boundary, year_data, buildings_data))