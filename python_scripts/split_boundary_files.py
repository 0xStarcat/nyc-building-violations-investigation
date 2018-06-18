import json

manhattan_features = []
bronx_features = []
brooklyn_features = []
queens_features = []
staten_island_features = []

def splitFeatureByBoroCode(feature):

  def appendManhattan():
    manhattan_features.append(feature)

  def appendBronx():
    bronx_features.append(feature)

  def appendBrooklyn():
    brooklyn_features.append(feature)

  def appendQueens():
    queens_features.append(feature)

  def appendStatenIsland():
    staten_island_features.append(feature)


  if "boroughCode" in feature["properties"]: # neighborhoods.geojson
    if feature["properties"]["boroughCode"] == "1":
      appendManhattan()
    elif feature["properties"]["boroughCode"] == "2":
      appendBronx()
    elif feature["properties"]["boroughCode"] == "3":
      appendBrooklyn()
    elif feature["properties"]["boroughCode"] == "4":
      appendQueens()
    elif feature["properties"]["boroughCode"] == "5":
      appendStatenIsland()
    else:
      print("  * Couldn't match " + feature["properties"]["boroughCode"])

  elif "BoroCode" in feature["properties"]: # census_tract_2010.geojson
    if feature["properties"]["BoroCode"] == "1":
      appendManhattan()
    elif feature["properties"]["BoroCode"] == "2":
      appendBronx()
    elif feature["properties"]["BoroCode"] == "3":
      appendBrooklyn()
    elif feature["properties"]["BoroCode"] == "4":
      appendQueens()
    elif feature["properties"]["BoroCode"] == "5":
      appendStatenIsland()
    else:
      print("  * Couldn't match " + feature["properties"]["BoroCode"])
  else:
    print("    * Couldn't find a code!")
with open("data/boundary_data/neighborhoods/neighborhoods.geojson") as neighborhood_data:
  manhattan_features = []
  bronx_features = []
  brooklyn_features = []
  queens_features = []
  staten_island_features = []

  neighborhood_json = json.load(neighborhood_data)
  print("Neighborhood data loaded with " + str(len(neighborhood_json["features"])) + " features")

  for feature in neighborhood_json["features"]:
    splitFeatureByBoroCode(feature)

  with open("data/boundary_data/neighborhoods/manh_neighborhoods.geojson", "w") as manhattan_neighborhood_data:
    neighborhood_json["features"] = manhattan_features
    json.dump(neighborhood_json, manhattan_neighborhood_data, sort_keys=True, indent=2)
    print("  Manhattan boundary data saved " + str(len(manhattan_features)) + " features")

  with open("data/boundary_data/neighborhoods/bx_neighborhoods.geojson", "w") as bronx_neighborhood_data:
    neighborhood_json["features"] = bronx_features
    json.dump(neighborhood_json, bronx_neighborhood_data, sort_keys=True, indent=2)
    print("  Bronx boundary data saved " + str(len(bronx_features)) + " features")

  with open("data/boundary_data/neighborhoods/bk_neighborhoods.geojson", "w") as brooklyn_neighborhood_data:
    neighborhood_json["features"] = brooklyn_features
    json.dump(neighborhood_json, brooklyn_neighborhood_data, sort_keys=True, indent=2)
    print("  Brooklyn boundary data saved " + str(len(brooklyn_features)) + " features")

  with open("data/boundary_data/neighborhoods/qns_neighborhoods.geojson", "w") as queens_neighborhood_data:
    neighborhood_json["features"] = queens_features
    json.dump(neighborhood_json, queens_neighborhood_data, sort_keys=True, indent=2)
    print("  Queens boundary data saved " + str(len(queens_features)) + " features")

  with open("data/boundary_data/neighborhoods/si_neighborhoods.geojson", "w") as staten_island_neighborhood_data:
    neighborhood_json["features"] = staten_island_features
    json.dump(neighborhood_json, staten_island_neighborhood_data, sort_keys=True, indent=2)
    print("  Staten Island boundary data saved " + str(len(staten_island_features)) + " features")

  print("Neighborhood data splitting completed.")


with open("data/boundary_data/census_tracts/census_tracts_2010.geojson") as census_tract_data:
  manhattan_features = []
  bronx_features = []
  brooklyn_features = []
  queens_features = []
  staten_island_features = []

  census_tract_json = json.load(census_tract_data)
  print("Census tract data loaded with " + str(len(census_tract_json["features"])) + " features")

  for feature in census_tract_json["features"]:
    splitFeatureByBoroCode(feature)

  with open("data/boundary_data/census_tracts/manh_census_tracts_2010.geojson", "w") as manhattan_neighborhood_data:
    neighborhood_json["features"] = manhattan_features
    json.dump(neighborhood_json, manhattan_neighborhood_data, sort_keys=True, indent=2)
    print("  Manhattan boundary data saved " + str(len(manhattan_features)) + " features")

  with open("data/boundary_data/census_tracts/bx_census_tracts_2010.geojson", "w") as bronx_neighborhood_data:
    neighborhood_json["features"] = bronx_features
    json.dump(neighborhood_json, bronx_neighborhood_data, sort_keys=True, indent=2)
    print("  Bronx boundary data saved " + str(len(bronx_features)) + " features")

  with open("data/boundary_data/census_tracts/bk_census_tracts_2010.geojson", "w") as brooklyn_neighborhood_data:
    neighborhood_json["features"] = brooklyn_features
    json.dump(neighborhood_json, brooklyn_neighborhood_data, sort_keys=True, indent=2)
    print("  Brooklyn boundary data saved " + str(len(brooklyn_features)) + " features")

  with open("data/boundary_data/census_tracts/qns_census_tracts_2010.geojson", "w") as queens_neighborhood_data:
    neighborhood_json["features"] = queens_features
    json.dump(neighborhood_json, queens_neighborhood_data, sort_keys=True, indent=2)
    print("  Queens boundary data saved " + str(len(queens_features)) + " features")

  with open("data/boundary_data/census_tracts/si_census_tracts_2010.geojson", "w") as staten_island_neighborhood_data:
    neighborhood_json["features"] = staten_island_features
    json.dump(neighborhood_json, staten_island_neighborhood_data, sort_keys=True, indent=2)
    print("  Staten Island boundary data saved " + str(len(staten_island_features)) + " features")

  print("Census tract data splitting completed")