import csv
from collections import Counter

import pandas as pd

sales_csv = pd.read_csv("data/sales_data/csv/bk_violation_before_property_sales_2011_2017.csv")

address_column = sales_csv.groupby("ADDRESS").size().reset_index(name='count').values.tolist()



# print(address_column)

# print(Counter.count(address_column))

duplicates_list = []
for x in address_column:
  if x[1] > 1:
    duplicates_list.append(x)

print(str(len(duplicates_list)))


# sales_data = list(csv.reader(open("data/sales_data/csv/bk_violation_before_property_sales_2011_2017.csv", "r")))

# list_data = []
# for row in sales_data:
#   list_data.append(row)

# sales_column_counts = dict(Counter(list_data))
# print(sales_column_counts)