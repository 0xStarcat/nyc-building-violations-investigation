import csv
import json
# Requires data tables containing all the sales and all residential buildings

count = 0
matches = 0
sales_data = list(csv.reader(open("data/sales_data/bk_property_sales_2011_2017.csv", "r")))

buildings_data = json.load(open("data/buildings_data/json/bk_buildings_by_block.json"))
filtered_sales_data = []

def find_block_and_lot_match(sale):
  return find_block_match(sale)

def find_block_match(sale):
  block_match = next((block for block in buildings_data["Block"] if str(sale[4]) == block["Block"]), False)
  if block_match:
    return find_lot_match(sale, block_match)
  else:
    return
    # print("  * No block found: " + sale[4])

def find_lot_match(sale, block):
  lot_match = next((lot for lot in block["features"] if str(sale[5]) == str(lot["properties"]["Lot"])), False)
  if lot_match:
    return lot_match
  else:
    return
    # print("  * No Lot found: " + sale[5])


for sale in sales_data:
  print("Processing sale: " + str(count) + "/" + str(len(sales_data)) + ' including: ' + str(matches))
  count += 1
  match = find_block_and_lot_match(sale)
  if match:
    filtered_sales_data.append(sale)
    matches += 1
    # print("Match found")
  else:
    continue

new_csv = csv.writer(open("data/sales_data/bk_residential_property_sales_2011_2017.csv", "w"))
headers = ["BOROUGH","NEIGHBORHOOD","BUILDING CLASS CATEGORY","TAX CLASS AT PRESENT","BLOCK","LOT","EASE-MENT","BUILDING CLASS AT PRESENT","ADDRESS","APARTMENT NUMBER","ZIP CODE","RESIDENTIAL UNITS","COMMERCIAL UNITS","TOTAL UNITS","LAND SQUARE FEET","GROSS SQUARE FEET","YEAR BUILT","TAX CLASS AT TIME OF SALE","BUILDING CLASS AT TIME OF SALE","SALE PRICE","SALE DATE"]
new_csv.writerow(headers)
for row in filtered_sales_data:
  new_csv.writerow(row)


