import json

index_list = []

def create_or_append_to_index_list(feature_data, index_key):
  if index_key in feature_data["properties"]:
    match = next((b for b in index_list if b[index_key] == str(feature_data["properties"][index_key])), False)
    if match == False:
      create_index_list(feature_data, index_key)
    else:
      print("    Found match " + str(match[index_key]))
      match["features"].append(feature_data)
  return

def create_index_list(feature_data, index_key):
  print("  Index " + str(feature_data["properties"][index_key]) + " created")
  index_list.append({index_key: str(feature_data["properties"][index_key]), "features": [feature_data]})
  return

def process_pluto_data(pluto_features, index_key):
  process_count = 0
  for f in pluto_features:
    print(str(process_count) + "/" + str(len(pluto_features)))
    process_count += 1
    if "properties" in f:
      create_or_append_to_index_list(f, index_key)
  return

def write_json(dest_file, index_key):
  with open(dest_file + ".json", "w") as out_data:
    print("Writing data to " + dest_file)
    data = {
      index_key: index_list
    }
    json.dump(data, out_data, sort_keys=True, indent=2)

# index_by_key("data/buildings_data/processed_mappluto.geojson", "data/buildings_data/bk_mappluto_by_block.json", "blocks")
def index_by_key(source_file, dest_file, index_key):
  print("Indexing by: " + index_key)
  with open(source_file) as mappluto_file:
    print(source_file + " loaded")
    pluto_data = json.load(mappluto_file)

    process_pluto_data(pluto_data["features"], index_key)
    print(str(len(index_list)) + " indexed")

    write_json(dest_file, index_key)
    print("Features indexed")

