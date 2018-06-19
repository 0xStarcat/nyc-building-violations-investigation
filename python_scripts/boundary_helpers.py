import json
import csv
import pandas as pd
import math
import index_data
from shapely.geometry import shape, Point

import importlib.machinery

from csv_generators import bk_new_and_total_buildings_by_census_tract_generator
from geojson_generators import bk_new_buildings
from geojson_generators import bk_new_buildings_by_census_tract


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

def process_median_income_data():
  income_data = []
  with open("data/boundary_data/geojson/bk_census_tracts_2010.geojson") as tract_data:
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

  with open("data/boundary_data/geojson/bk_census_tracts_2010.geojson") as tract_data:
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

  with open("data/boundary_data/geojson/bk_census_tracts_2010.geojson", "w") as new_tract_data:
      json.dump(tract_json, new_tract_data, sort_keys=True, indent=2)

def add_computed_violation_data_to_census_tracts():
  tract_json = {}
  violations_data = []

  with open("data/boundary_data/geojson/bk_census_tracts_2010.geojson") as tract_data:
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
      tract["properties"]["2017"] = {} 
      tract["properties"]["2017"]["violationsPerBuilding"] = match[12]
      tract["properties"]["2017"]["totalBuildings"] = match[9]
      print("  * match found: " + tract["properties"]["CTLabel"])

  with open("data/boundary_data/geojson/bk_census_tracts_2010.geojson", "w") as new_tract_data:
      print("Writing JSON")
      json.dump(tract_json, new_tract_data, sort_keys=True, indent=2)

def process_files_new_buildings_by_year_and_total():
  tract_buildings_json = {}
  years_data = ["2011", "2012", "2013", "2014", "2015", "2016", "2017"]
  buildings_data = []
  new_buildings_data = []

  def process_data(tract_data):
    total_buildings = 0 # Count all the buildings
    total_pre_2011_buildings = 0 # Count all pre-2011 buildings
    buildings_2011 = []
    buildings_2012 = []
    buildings_2013 = [] 
    buildings_2014 = [] 
    buildings_2015 = [] 
    buildings_2016 = [] 
    buildings_2017 = []
    number_new_buildings_2011_2017 = 0 # Count how many buildings added over the years

    for building in tract_data["features"]:
      print("buildings processed: " + str(total_buildings) + " / " + str(len(tract_data["features"])))

      total_buildings += 1
      if int(building["properties"]["YearBuilt"]) < 2011:
        total_pre_2011_buildings += 1
      if int(building["properties"]["YearBuilt"]) == 2011:
        buildings_2011.append(building)
        new_buildings_data.append(building)
      if int(building["properties"]["YearBuilt"]) == 2012:
        buildings_2012.append(building)
        new_buildings_data.append(building)
      if int(building["properties"]["YearBuilt"]) == 2013:
        buildings_2013.append(building)
        new_buildings_data.append(building)
      if int(building["properties"]["YearBuilt"]) == 2014:
        buildings_2014.append(building)
        new_buildings_data.append(building)
      if int(building["properties"]["YearBuilt"]) == 2015:
        buildings_2015.append(building)
        new_buildings_data.append(building)
      if int(building["properties"]["YearBuilt"]) == 2016:
        buildings_2016.append(building)
        new_buildings_data.append(building)
      if int(building["properties"]["YearBuilt"]) == 2017:
        buildings_2017.append(building)
        new_buildings_data.append(building)

    print("Buildings found for tract: " + tract_data["CT2010"] + " - ", total_buildings, total_pre_2011_buildings, len(buildings_2011), len(buildings_2012), len(buildings_2013), len(buildings_2014), len(buildings_2015), len(buildings_2016), len(buildings_2017), number_new_buildings_2011_2017)

    number_new_buildings_2011_2017 = total_buildings - total_pre_2011_buildings
    buildings_data.append([tract_data["CT2010"], len(buildings_2011), len(buildings_2012), len(buildings_2013), len(buildings_2014), len(buildings_2015), len(buildings_2016), len(buildings_2017), number_new_buildings_2011_2017, total_pre_2011_buildings, total_buildings])

  with open("data/buildings_data/bk_buildings_by_census_tract.json") as tract_buildings_data:
      tract_buildings_json = json.load(tract_buildings_data)

  for tract_data in sorted(tract_buildings_json["CT2010"], key=lambda obj: obj["CT2010"]):
    process_data(tract_data)

  print(buildings_data[0])

  bk_new_and_total_buildings_by_census_tract_generator.generate_csv(buildings_data, years_data)
  bk_new_buildings.generate_geojson(new_buildings_data)
  bk_new_buildings_by_census_tract.generate_geojson()

