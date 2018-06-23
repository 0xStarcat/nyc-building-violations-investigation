import csv
import json
import datetime
# Requires data tables containing all the sales and all residential buildings

count = 0
matches = 0
sales_data = list(csv.reader(open("data/sales_data/csv/bk_violation_property_sales_2011_2017.csv", "r")))

violations_data = json.load(open("data/violations_data/json/bk_nyc_dob_violation_data_by_block.json"))
filtered_sales_data = []

def find_blockand_violation_before_sale_match(sale):
  return find_block_match(sale)

def find_block_match(sale):
  block_match = next((block for block in violations_data["block"] if str(sale[4]) == str(block["block"]).lstrip("0")), False)
  if block_match:
    return find_violation_before_sale(sale, block_match)
  else:
    return
    # print("  * No block found: " + sale[4])

def find_violation_in_date_range(sale, violation):
  sale_date = datetime.datetime.strptime(str(sale[20]), '%m/%d/%Y')
  violation_date = datetime.datetime.strptime(str(violation["properties"]["issue_date"]), '%Y%m%d')
  return sale_date > violation_date

def find_violation_before_sale(sale, block):
  return next((violation for violation in block["features"] if find_violation_in_date_range(sale, violation)), False)

for sale in sales_data:
  print("Processing sale: " + str(count) + "/" + str(len(sales_data)) + ' including: ' + str(matches))
  count += 1
  match = find_blockand_violation_before_sale_match(sale)
  if match:
    filtered_sales_data.append(sale)
    matches += 1
    print("Match found with sale date: " + sale[20] + " and violation date: " + match["properties"]["issue_date"])
  else:
    continue

new_csv = csv.writer(open("data/sales_data/csv/bk_violation_before_property_sales_2011_2017.csv", "w"))
headers = ["BOROUGH","NEIGHBORHOOD","BUILDING CLASS CATEGORY","TAX CLASS AT PRESENT","BLOCK","LOT","EASE-MENT","BUILDING CLASS AT PRESENT","ADDRESS","APARTMENT NUMBER","ZIP CODE","RESIDENTIAL UNITS","COMMERCIAL UNITS","TOTAL UNITS","LAND SQUARE FEET","GROSS SQUARE FEET","YEAR BUILT","TAX CLASS AT TIME OF SALE","BUILDING CLASS AT TIME OF SALE","SALE PRICE","SALE DATE"]
new_csv.writerow(headers)
for row in filtered_sales_data:
  new_csv.writerow(row)

