import json
from shapely.geometry import shape, Point

def add_neighborhood_property_to_feature(feature, neighborhood_json):
  matching_ct = next((neighborhood for neighborhood in neighborhood_json["features"] if shape(neighborhood["geometry"]).contains(Point(feature["geometry"]["coordinates"]))), False) 
  if matching_ct == False:
    if "properties" in feature:
      feature["properties"]["neighborhood"] = ""
    else:
      feature["neighborhood"] = ""
    return
  else:
    if "properties" in feature:
      feature["properties"]["neighborhood"] = matching_ct["properties"]["neighborhood"]
    else:
      feature["neighborhood"] = ""

def add_census_tract_property_to_feature(feature, census_tract_json):
  matching_ct = next((neighborhood for neighborhood in census_tract_json["features"] if shape(neighborhood["geometry"]).contains(Point(feature["geometry"]["coordinates"]))), False) 
  if matching_ct == False:
    if "properties" in feature:
      feature["properties"]["neighborhood"] = ""
    else:
      feature["neighborhood"] = ""
    return
  else:
    if "properties" in feature:
      feature["properties"]["neighborhood"] = matching_ct["properties"]["neighborhood"]
    else:
      feature["neighborhood"] = ""


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


add_neighborhood_to_census_tract()