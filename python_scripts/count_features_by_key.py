import csv
import json

key_list = []

def create_or_append_to_key_list(feature, key):
  if not feature["properties"][key]:
    return
  else:
    match = next((entry for entry in key_list if entry[key] == str(feature["properties"][key])), False)
    if match == False:
      create_key_entry(feature, key)
    else:
      print("    Found match " + str(match[key]))
      match["features"].append(feature)

def create_key_entry(feature, key):
  key_list.append({key: str(feature["properties"][key]), "features": [feature]})
  print("  " + str(feature["properties"][key]) + " created")

def write_json(dest_file, key, key_list):
  with open(dest_file + ".json", "w") as outjson:
    print("writing JSON to: " + dest_file)

    data = {
      key: key_list
    }

    json.dump(data, outjson, sort_keys=True, indent=2)

  with open(dest_file + "_totals.json", "w") as outjson:
    print("writing JSON counts to: " + dest_file + "_counts.json")
    new_key_list = [] 
    for entry in key_list:
      new_entry = entry
      new_entry["numFeatures"] = len(entry["features"])
      new_entry.pop("features", None)
      new_key_list.append(entry)

    data = {
      key: new_key_list
    }

    json.dump(data, outjson, sort_keys=True, indent=2)

def write_csv(dest_file, key, key_list):
  with open(dest_file, 'w') as outcsv:
    def sort_by_key(obj):
          return obj[key]

    print("writing to CSV to: " + dest_file)
    writer = csv.writer(outcsv)
    writer.writerow([key, "Features"])

    for entry in sorted(key_list, key=sort_by_key):
      writer.writerow([entry[key], len(entry["features"])])


def count_by_key(source_file, dest_file, key):
  with open(source_file) as source_data:
    source_json = json.load(source_data)
    print("Data loaded")
    process_count = 0
    for feature in source_json["features"]:
      print(str(process_count) + "/" + str(len(source_json["features"])))
      create_or_append_to_key_list(feature, key)
      process_count += 1

  write_csv(dest_file, key, key_list)

  # write_json(dest_file, key, key_list)
