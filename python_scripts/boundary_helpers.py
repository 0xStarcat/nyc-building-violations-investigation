import json
import csv
import pandas as pd
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
      tract["properties"]["median_income_2010"] = match[1] 
      tract["properties"]["median_income_2017"] = match[2] 
      print("  * match found: " + tract["properties"]["CT2010"])

  with open("data/boundary_data/census_tracts/bk_census_tracts_2010.geojson", "w") as new_tract_data:
      json.dump(tract_json, new_tract_data, sort_keys=True, indent=2)

  print(tract_json["features"][0])

def add_properties_to_neighborhood_from_census_tract():