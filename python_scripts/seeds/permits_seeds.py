import json
import buildings_seeds
from shapely.geometry import Point, mapping
import datetime
permits_table = 'permits'

def get_geometry(permit):
  if permit[14] and permit[13]:
    return mapping(Point(float(permit[14]), float(permit[13])))
  else:
    return None

def get_building_match(c, permit):
  c.execute('SELECT * FROM buildings WHERE block={v_block} AND lot={v_lot}'.format(v_block=str(permit[3]), v_lot=str(permit[23])))
  return c.fetchone()

def convert_date_format(permit):
  return datetime.datetime.strptime(permit[18][:10], "%Y-%m-%d").strftime("%Y%m%d")

def seed_permits(c, permit_csv):
  print("Seeding permits...")
  permit_col1 = 'building_id'
  permit_col2 = 'issue_date'
  permit_col3 = 'geometry'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER REFERENCES {bldg_table}(id), {col2} TEXT, {col3} INT)'\
    .format(tn=permits_table, col1=permit_col1, col2=permit_col2, col3=permit_col3, bldg_table=buildings_seeds.buildings_table))

  c.execute('CREATE INDEX idx_permit_building_id ON {tn}({col1})'.format(tn=permits_table, col1=permit_col1))

  for index, permit in enumerate(permit_csv):
    print("permit: " + str(index) + "/" + str(len(permit_csv)))
    
    building_match = get_building_match(c, permit)

    if not building_match:
      print("  - no building match found")


    building_id = building_match[0] if building_match else None
    issue_date = convert_date_format(permit)
    geometry = get_geometry(permit)
    
    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}) VALUES (?, ?, ?)'\
      .format(tn=permits_table, col1=permit_col1, col2=permit_col2, col3=permit_col3), (building_id, str(issue_date), str(geometry)))

    

