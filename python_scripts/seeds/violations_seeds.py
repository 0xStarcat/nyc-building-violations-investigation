import json
import buildings_seeds

violations_table = 'violations'

def get_description(violation):
  description = ""
  if "violation_description" in violation:
    description = violation["violation_description"]
  elif "description" in violation:
    description = violation["description"]
  else:
    # print("  * No description found")
    pass
  return description

def get_building_match(c, violation):
  if "block" in violation and "lot" in violation and violation["block"].lstrip("0") and violation["lot"].lstrip("0"):
    c.execute('SELECT * FROM buildings WHERE block={v_block} AND lot={v_lot}'.format(v_block=violation["block"].lstrip("0"), v_lot=violation["lot"].lstrip("0")))
    return c.fetchone()
  else:
    return None

def seed_violations(c, violation_json):
  print("Seeding Violations...")
  vio_col1 = 'building_id'
  vio_col2 = 'issue_date'
  vio_col3 = 'description'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {bldg_table}(id), {col2} TEXT, {col3} TEXT)'\
    .format(tn=violations_table, col1=vio_col1, col2=vio_col2, col3=vio_col3, bldg_table=buildings_seeds.buildings_table))

  c.execute('CREATE INDEX idx_violation_building_id ON {tn}({col1})'.format(tn=violations_table, col1=vio_col1))

  for index, violation in enumerate(violation_json):
    print("Violation: " + str(index) + "/" + str(len(violation_json)))
    
    building_match = get_building_match(c, violation)

    # building_match = lot_match(violation["lot"].lstrip("0"), buildings_by_block)
    if building_match:
      pass
    else: 
      print("  * no building match found")
      continue

    building_id = building_match[0]
    if "issue_date" not in violation:
      print("  * no issue_date found")
      continue
    issue_date = violation["issue_date"]
    description = get_description(violation)
    
    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}) VALUES ({building_id}, \'{issue_date}\', \"{description}\")'\
      .format(tn=violations_table, col1=vio_col1, col2=vio_col2, col3=vio_col3, building_id=building_id, issue_date=issue_date, description=description))