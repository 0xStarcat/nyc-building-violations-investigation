import json
import buildings_seeds

sales_table = 'sales'

def get_price(sale):
  price = 0
  if sale[19]:
    price = sale[19].replace(",", "").replace(".", "").replace(" ", "").replace("-", "").lstrip("$")
  else:
    # print("  * No price found")
    pass
  return price

def get_building_match(c, sale):
  c.execute('SELECT * FROM buildings WHERE block={v_block} AND lot={v_lot}'.format(v_block=str(sale[4]), v_lot=str(sale[5])))
  return c.fetchone()


def seed_sales(c, sale_csv):
  print("Seeding sales...")
  sale_col1 = 'building_id'
  sale_col2 = 'sale_date'
  sale_col3 = 'price'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {bldg_table}(id), {col2} TEXT, {col3} INT)'\
    .format(tn=sales_table, col1=sale_col1, col2=sale_col2, col3=sale_col3, bldg_table=buildings_seeds.buildings_table))

  c.execute('CREATE INDEX idx_sale_building_id ON {tn}({col1})'.format(tn=sales_table, col1=sale_col1))

  for index, sale in enumerate(sale_csv):
    print("sale: " + str(index) + "/" + str(len(sale_csv)))
    
    building_match = get_building_match(c, sale)

    if building_match:
      pass
    else: 
      print("  * no building match found")
      continue

    building_id = building_match[0]
    sale_date = sale[20]
    price = get_price(sale)
    
    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}) VALUES ({building_id}, \'{sale_date}\', \"{price}\")'\
      .format(tn=sales_table, col1=sale_col1, col2=sale_col2, col3=sale_col3, building_id=building_id, sale_date=sale_date, price=price))

    

