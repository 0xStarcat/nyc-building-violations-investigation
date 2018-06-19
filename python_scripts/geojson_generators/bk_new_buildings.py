import json

def generate_geojson(new_buildings_data):
  with open("data/buildings_data/geojson/bk_new_buildings.geojson", "w") as geo_json_file:
    geo_data = {
      "crs": {
        "properties": {
          "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        },
        "type": "name",
        "name": "new_and_total_buildings_geodata",
        "type": "FeatureCollection"
      },
      "features": new_buildings_data
    }

    json.dump(geo_data, geo_json_file, sort_keys=True, indent=2)