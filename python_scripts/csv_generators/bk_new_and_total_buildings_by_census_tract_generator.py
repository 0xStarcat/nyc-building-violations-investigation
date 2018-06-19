import csv

def generate_csv(buildings_data, years_data):
  with open("data/buildings_data/csv/bk_new_and_total_buildings_by_census_tract.csv", "w") as new_buildings_csv:
    print("Writing CSV")
    csv_writer = csv.writer(new_buildings_csv)
    csv_writer.writerow(["CT2010"] + years_data + ["Total new buildings 2011 - 2017", "Total Pre2011 Buildings", "Total Buildings"])

    for tract_data in sorted(buildings_data, key=lambda obj: obj[0]):
      csv_writer.writerow(tract_data)

def generate_row(tract_data):
  matching_row = next((data for data in buildings_data if data[0] == tract_data["CT2010"]), False)
  if matching_row == False:
    print("  * Matching row not found!! Error!")
  else:
    return matching_row