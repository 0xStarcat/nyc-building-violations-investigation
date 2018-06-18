# Should return a CSV and a JSON object containing:
# Boundary name
# Num of violations
# Num of buildings
# Num of violations in Year 1
# Num of violations in Year 2,
# etc...


import json
import csv
import count_features_by_boundary


def generate_neighborhood_report():

  # Grab building data
  building_data = []
  with open('data/buildings_data/bk_residential_buildings_by_neighborhood.csv') as buildings_csv:
    building_data = csv.reader(buildings_csv, delimiter=',')
    for row in building_data:
      print(row)










generate_neighborhood_report() 