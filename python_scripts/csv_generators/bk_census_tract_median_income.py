import pandas as pd
import csv 

def read_csv(source):
  return pd.read_csv(source, sep=',',header=1)

def generate_csv():
  # 2010 median income
  # 2017 median income
  # Change from 2010 - 2017
  income_data = []

  # read income CSV
  income_csv = read_csv("data/demographic_data/bk_median_income_2017.csv")
  print("csv loaded")

  def generate_row(income_row):
    ct_id = str(int(income_row[0]))[5:]
    mi_2011 = round(float(income_row[1]), 2)
    mi_2017 = round(float(income_row[2]), 2)
    change_2011_2017 = round(mi_2017 - mi_2011, 2)
    return [ct_id, mi_2011, mi_2017, change_2011_2017]

  # write CSV
  with open('data/demographic_data/csv/bk_census_tract_median_income.csv', 'w') as outcsv:
    print("writing to CSV")
    writer = csv.writer(outcsv)
    writer.writerow(["CT2010", "Median Income 2011", "Median Income 2017", "Change 2011-2017"])
    for index, row in income_csv.iterrows():
      writer.writerow(generate_row(row))
