import json
import csv
import pandas as pd
import math
from shapely.geometry import shape, Point

def add_neighborhood_property_to_feature(feature, neighborhood_json):
  matching_ct = next((neighborhood for neighborhood in neighborhood_json["features"] if shape(neighborhood["geometry"]).contains(Point(feature["geometry"]["coordinates"]))), False) 
  if matching_ct == False:
    if "properties" in feature:
      feature["properties"]["neighborhood"] = None
    else:
      feature["neighborhood"] = None
    return
  else:
    if "properties" in feature:
      feature["properties"]["neighborhood"] = matching_ct["properties"]["neighborhood"]
    else:
      feature["neighborhood"] = None

def add_neighborhood_to_census_tract():
  neighborhood_json = {}
  with open("data/boundary_data/neighborhoods/bk_neighborhoods.geojson") as neighborhood_data:
    neighborhood_json = json.load(neighborhood_data)
    print("Neighborhood json loaded")


  with open("data/boundary_data/census_tracts/bk_census_tracts_2010.geojson") as tract_data:
    tract_json = json.load(tract_data)
    for tract in tract_json["features"]:
      match = next((neighborhood for neighborhood in neighborhood_json["features"] if shape(neighborhood["geometry"]).contains(Point(shape(tract["geometry"]).representative_point()))), False) 
      if match == False:
        print("  * no match for " + tract["properties"]["CTLabel"])
      else:
        tract["properties"]["neighborhood"] = match["properties"]["neighborhood"]
        print("match for " + tract["properties"]["CTLabel"])

    with open("data/boundary_data/census_tracts/bk_census_tracts_2010.geojson", "w") as new_tract_data:
      json.dump(tract_json, new_tract_data, sort_keys=True, indent=2)

def process_median_income_data():
  income_data = []
  with open("data/boundary_data/census_tracts/bk_census_tracts_2010.geojson") as tract_data:
    tract_json = json.load(tract_data)
    print("Tract json loaded")

  income_csv = pd.read_csv("data/demographic_data/censustract-medianhouseholdincome2017.csv", sep=',',header=None)  
  for total in income_csv.values:
    total=total[2:5]
    if total[0][:5] == "36047":
      income_data.append(total)

  with open("data/demographic_data/bk_median_income_2017.csv", "w") as new_income_data:
    writer = csv.writer(new_income_data)
    writer.writerow(["CT2010", "2010", "2016"])

    for income in income_data:
      writer.writerow(income)

def add_median_income_to_census_tracts():
  tract_json = {}
  income_data = []

  with open("data/boundary_data/census_tracts/bk_census_tracts_2010.geojson") as tract_data:
    tract_json = json.load(tract_data)
    print("Tract json loaded")

  income_csv = pd.read_csv("data/demographic_data/bk_median_income_2017.csv", sep=',',header=None)  
  for total in income_csv.values:
    income_data.append(total)

  income_data.pop(0)

  for tract in tract_json["features"]:
    match = next((income for income in income_data if tract["properties"]["CT2010"] == str(income[0][5:])), []) 
    if len(match) == 0:
      print("  * could not match tract: " + tract["properties"]["CT2010"])
    else:
      if math.isnan(match[1]) or math.isnan(match[2]):
        tract["properties"]["median_income_2010"] = None
        tract["properties"]["median_income_2017"] = None 
      else:
        tract["properties"]["median_income_2010"] = match[1] 
        tract["properties"]["median_income_2017"] = match[2] 
        print("  * match found: " + tract["properties"]["CT2010"])

  with open("data/boundary_data/census_tracts/bk_census_tracts_2010.geojson", "w") as new_tract_data:
      json.dump(tract_json, new_tract_data, sort_keys=True, indent=2)

def add_computed_violation_data_to_census_tracts():
  tract_json = {}
  violations_data = []

  with open("data/boundary_data/census_tracts/bk_census_tracts_2010.geojson") as tract_data:
    tract_json = json.load(tract_data)
    print("Tract json loaded")

  violation_csv = pd.read_csv("data/violations_data/bk_census_tract_violations_by_year.csv", sep=',',header=None)

  for tract in violation_csv.values:
    violations_data.append(tract)

  violations_data.pop(0)

  for tract in tract_json["features"]:
    print(violations_data[0])
    match = next((entry for entry in violations_data if entry[0] == tract["properties"]["CTLabel"]), []) 
    if len(match) <= 0:
      print("  * could not match tract: " + tract["properties"]["CTLabel"])
    else:
      tract["2017"] = {} 
      tract["2017"]["violationsPerBuilding"] = match[12]
      tract["2017"]["totalBuildings"] = match[9]
      print("  * match found: " + tract["properties"]["CTLabel"])

  with open("data/boundary_data/census_tracts/bk_census_tracts_2010.geojson", "w") as new_tract_data:
      print("Writing JSON")
      json.dump(tract_json, new_tract_data, sort_keys=True, indent=2)



