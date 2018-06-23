import csv
import json
from shapely.geometry import shape, Point

def match_census_tract_to_neighborhood(tract, neighborhood_json):
  match = next((neighborhood for neighborhood in neighborhood_json["features"] if shape(neighborhood["geometry"]).contains(Point(shape(tract["geometry"]).representative_point()))), False) 
  if match == False:
    print("  * no match for " + tract["properties"]["CTLabel"])
  else:
    return match["properties"]["neighborhood"]
    print("match for " + tract["properties"]["CTLabel"])

def get_value_from_matching_row(tract, value_index, property_attribute, csv_data):
  match = next((row for row in csv_data if str(row[0]) == str(tract["properties"][property_attribute])), False)
  if match:
    # print("match for " + tract["properties"][property_attribute])
    return match[value_index]
  else:
    print("  * no match for " + tract["properties"][property_attribute])

def fill_json():
  income_csv = list(csv.reader(open('data/demographic_data/csv/bk_census_tract_median_income.csv', 'r')))
  buildings_csv = list(csv.reader(open('data/buildings_data/csv/bk_new_and_total_buildings_by_census_tract.csv', 'r')))
  
  neighborhood_json = json.load(open("data/boundary_data/geojson/bk_neighborhoods.geojson", 'r'))
  
  tract_json = json.load(open('data/boundary_data/geojson/bk_census_tracts_2010.geojson', 'r'))

  for tract in tract_json["features"]:
    if "medianIncomeChange20102017" in tract["properties"]:
      del tract["properties"]["medianIncomeChange20102017"]

    if "totalNewBuildings20102017" in tract["properties"]:
      del tract["properties"]["totalNewBuildings20102017"]

    tract["properties"]["neighborhood"] = match_census_tract_to_neighborhood(tract, neighborhood_json)
    tract["properties"]["medianIncome2011"] = get_value_from_matching_row(tract, 1, "CT2010", income_csv)
    tract["properties"]["medianIncome2017"] = get_value_from_matching_row(tract, 2, "CT2010", income_csv)
    tract["properties"]["medianIncomeChange"] = get_value_from_matching_row(tract, 3, "CT2010", income_csv)
    tract["properties"]["totalBuildings"] = get_value_from_matching_row(tract, 10, "CTLabel", buildings_csv)
    tract["properties"]["pre2011Buildings"] = get_value_from_matching_row(tract, 9, "CTLabel", buildings_csv)
    tract["properties"]["totalNewBuildings"] = get_value_from_matching_row(tract, 8, "CTLabel", buildings_csv)
    tract["properties"]["totalBuildingSales"] = ""
    tract["properties"]["totalViolationBuildingSales"] = ""

  new_json = tract_json
  with open('data/boundary_data/geojson/bk_census_tracts_2010.geojson', 'w') as out_json:
    print("writing JSON")
    json.dump(new_json, out_json, sort_keys=True, indent=2)

fill_json()

  # fieldnames = ("FirstName","LastName","IDNumber","Message")
  # reader = csv.DictReader( csvfile, fieldnames)
  # for row in reader:
  #     json.dump(row, jsonfile)
  #     jsonfile.write('\n')