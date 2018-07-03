import json
import buildings_seeds
import building_events_seeds
import datetime

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

def get_penalty(violation):
  penalty_imposed = ""
  if "penality_imposed" in violation:
    if violation["penality_imposed"] == ".00":
      pass
    else:
      penalty_imposed = violation["penality_imposed"]

  return penalty_imposed

def get_date(violation):
  if "issue_date" in violation:
    return violation["issue_date"]
  elif "inspectiondate" in violation:
    return datetime.datetime.strptime(violation['inspectiondate'][:10], "%Y-%m-%d").strftime("%Y%m%d")
  else:
    return False

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
  vio_col4 = 'penalty_imposed'
  vio_col5 = 'source'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {bldg_table}(id), {col2} TEXT, {col3} TEXT, {col4} TEXT, {col5} TEXT)'\
    .format(tn=violations_table, col1=vio_col1, col2=vio_col2, col3=vio_col3, col4=vio_col4,col5=vio_col5, bldg_table=buildings_seeds.buildings_table))

  c.execute('CREATE INDEX idx_violation_building_id ON {tn}({col1})'.format(tn=violations_table, col1=vio_col1))
  c.execute('CREATE INDEX idx_violation_source ON {tn}({col5})'.format(tn=violations_table, col5=vio_col5))

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
    
    issue_date = get_date(violation)

    if issue_date == False:
      print("  * no issue_date or inspectiondate found")
      continue

    description = get_description(violation)

    penalty_imposed = get_penalty(violation)
    source = violation['source']
    
    # Create Violation
    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}, {col5}) VALUES ({building_id}, \'{issue_date}\', \"{description}\", \'{penalty_imposed}\', \'{source}\')'\
      .format(tn=violations_table, col1=vio_col1, col2=vio_col2, col3=vio_col3, col4=vio_col4, col5=vio_col5, building_id=building_id, issue_date=issue_date, description=description, penalty_imposed=penalty_imposed, source=source))

    insertion_id = c.lastrowid

    c.execute('SELECT * FROM {tn} WHERE {cn}={b_id}'\
      .format(tn=buildings_seeds.buildings_table, cn='id', b_id=building_id))

    building = c.fetchone()

    # Create Building Event
    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}, {col5}, {col6}) VALUES ({ct_id}, {n_id}, {building_id}, \'{eventable}\', \"{event_id}\", \"{event_date}\")'\
      .format(tn=building_events_seeds.building_events_table, col1="census_tract_id", col2="neighborhood_id", col3="building_id", col4="eventable", col5="eventable_id", col6="event_date", ct_id=building[6], n_id=building[7], building_id=building_id, eventable='violation', event_id=insertion_id, event_date=issue_date))

