import json

count = 0

# Adds the Coordinates to the data

def lot_and_block_match(lot, block, block_list):
  block_match = next((b for b in block_list if block == b["Block"]), False)
  if block_match == False:
    print("  * no match found for block " + block)
    return False
  else:
    lot_match = next((l for l in block_match["features"] if lot == str(l["properties"]["Lot"])), False)
    if lot_match == False:
      return False
      print("    * no match found for block " + block + " and lot " + lot)
    else:
      return lot_match

with open("data/violations_data/bk_violation_data_2008_2017.json") as dob_data_json:
  with open("data/buildings_data/json/bk_buildings_by_block.json") as block_json:
    block_data = json.load(block_json)
    print("Block file loaded")
    violation_data = json.load(dob_data_json)
    print("Violated data loaded")

    new_data = {
      "crs": {
        "properties": {
          "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        },
        "type": "name",
        "name": "mappluto_violation_data",
        "type": "FeatureCollection"
      },
      "features": []
    }

    new_geo_data = {
      "crs": {
        "properties": {
          "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        },
        "type": "name",
        "name": "mappluto_violation_data",
        "type": "FeatureCollection"
      },
      "features": []
    }

    for violation in violation_data:
      print(str(count) + "/" + str(len(violation_data)) + " - " + str(len(new_data["features"])) + " matches found")
      count += 1
      if "lot" in violation and "block" in violation: 
        pluto_match = lot_and_block_match(violation["lot"].lstrip("0"), violation["block"].lstrip("0"), block_data["Block"])
        
        # BBL match - very slow
        # match = next((building for building in pluto_json["features"] if converted_BBL == str(int(building["properties"]["BBL"]))), False) 

        if pluto_match == False:
          continue 
        else:
          coordinates = pluto_match["geometry"]["coordinates"]
          
          new_violation_properties = {
            "properties": violation,
            "geometry": {
              "coordinates": coordinates,
              "type": "Point"
            },
            "type": "Feature"
          }

          new_violation_properties["properties"]["neighborhood"] = pluto_match["properties"]["neighborhood"]
          new_violation_properties["properties"]["CT2010"] = pluto_match["properties"]["CT2010"]

          new_violation_geo_data = {
            "geometry": {
              "coordinates": coordinates,
              "type": "Point"
            },
            "type": "Feature"
          }

          new_data["features"].append(new_violation_properties)
          new_geo_data["features"].append(new_violation_geo_data)
        
      else:
        continue



    with open("data/violations_data/json/processed_bk_violation_data_2008_2017.json", "w") as violation_geo_data:
      print("Writing property data: " + str(len(new_data["features"])) + " to file.")
      json.dump(new_data, violation_geo_data, sort_keys=True, indent=2)

    with open("data/violations_data/geojson/processed_bk_violation_data_2008_2017.geojson", "w") as violation_geo_data:
      print("Writing geo data: " + str(len(new_geo_data["features"])) + " to file.")
      json.dump(new_geo_data, violation_geo_data, sort_keys=True, indent=2)