import json 
import csv

from shapely.geometry import shape, Polygon, Point

def find_point_in_polygon(feature, boundary_features):
  return next((boundary for boundary in boundary_features if shape(boundary["geometry"]).contains(Point(feature["geometry"]["coordinates"]))), False)

def create_count_or_append_feature(feature, match, boundary_key, counts):
  count_match = next((nc for nc in counts if nc["name"] == str(match["properties"][boundary_key])), False)
  if count_match == False:
    print("  Sorted to new count entry: " + match["properties"][boundary_key]) 
    create_new_count_entry(match, feature, boundary_key, counts)
  else:
    count_match["features"].append(feature)
    print("  Adding new feature to existing entry " + match["properties"][boundary_key])
       
def create_new_count_entry(match, feature, boundary_key, counts):
  new_count = {
    "name": match["properties"][boundary_key],
    "features": [feature]
  }

  counts.append(new_count)

def write_counts_to_csv(output_file, boundary_key, counts):
  with open(output_file + '_totals.csv', 'w') as outcsv:
    print("writing to CSV")
    writer = csv.writer(outcsv)
    writer.writerow([boundary_key, "NumFeatures"])
    for count in counts:
      writer.writerow([count["name"], len(count["features"])])

def write_json_data(output_file, boundary_key, counts):
  with open(output_file + ".json", "w") as outjson:
    print("writing JSON")

    data = {
      boundary_key: counts
    }

    json.dump(data, outjson, sort_keys=True, indent=2)

  with open(output_file + "_totals.json", "w") as outjson:
    print("writing JSON counts")
    new_counts = [] 
    for count in counts:
      new_count = count
      new_count["numFeatures"] = len(count["features"])
      new_count.pop("features", None)
      new_counts.append(count)

    data = {
      boundary_key: new_counts
    }

    json.dump(data, outjson, sort_keys=True, indent=2)

def count_objects_by_boundary(features_file, boundaries_file, boundary_key, output_file, write):
  counts = []

  with open(features_file) as features_data:
    features_json = json.load(features_data)
    print("Features data loaded")
    with open(boundaries_file) as boundaries_data:
      boundaries_json = json.load(boundaries_data)
      print("Boundaries data loaded")

      count = 0
      for feature in features_json["features"]:
        print(str(count) + "/" + str(len(features_json["features"])))
        count += 1

        match = find_point_in_polygon(feature, boundaries_json["features"])
        
        if match == False:
          print("  * No matching boundary found in json")
        else:
          create_count_or_append_feature(feature, match, boundary_key, counts)
        
      
      if (write == True):
        def sort_by_name(obj):
          return obj["name"]

        
        # write CSV data
        write_counts_to_csv(output_file, boundary_key, sorted(counts, key=sort_by_name))

        # write JSON data
        write_json_data(output_file, boundary_key, counts)
      else:
        return counts


# count_objects_by_boundary("data/violations_data/nyc_violation_data_geo.geojson", "data/boundary_data/geojson/bk_neighborhoods.geojson", "neighborhood", "data/violations_data/violations_by_neighborhoods_count", True)