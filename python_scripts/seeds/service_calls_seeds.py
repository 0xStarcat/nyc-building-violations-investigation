import json
import buildings_seeds
import building_events_seeds
import datetime
service_calls_table = 'service_calls'

def call_is_duplicate(description):
  if "were addressed under another service request number" in description:
    return True
  elif "More than one complaint was received" in description:
    return True
  else:
    return False

def resulted_in_violation(description):
  if "violation" in description and "No violations were issued" not in description:
    return True
  elif "Violations" in description and "No violations were issued" not in description:
    return True
  else:
    return False

def unresolved_call(description):
  if "gain access" in description:
    return True
  elif "Please check back later for status" in description:
    return True
  else:
    return False

def took_no_action(description):
  if "No violations were issued" in description:
    return True
  elif "no further action was necessary" in description:
    return True
  else:
    return False

def get_building_match(c, address):
  c.execute('SELECT * FROM buildings WHERE address=\"{address}\"'.format(address=address))
  return c.fetchone()

def seed_service_calls(c, service_calls_csv):
  print("Seeding calls...")
  call_col1 = 'building_id'
  call_col2 = 'call_date'
  call_col3 = 'description'
  call_col4 = 'resolution_description'
  call_col5 = 'resolution_violation'
  call_col6 = 'resolution_no_action'
  call_col7 = 'unresolved'
  call_col8 = 'source'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {bldg_table}(id), {col2} TEXT, {col3} TEXT, {col4} TEXT, {col5} BOOLEAN, {col6} BOOLEAN, {col7} BOOLEAN, {col8} TEXT)'\
    .format(tn=service_calls_table, col1=call_col1, col2=call_col2, col3=call_col3, col4=call_col4, col5=call_col5, col6=call_col6, col7=call_col7, col8=call_col8, bldg_table=buildings_seeds.buildings_table))

  c.execute('CREATE INDEX idx_call_building_id ON {tn}({col1})'.format(tn=service_calls_table, col1=call_col1))
  c.execute('CREATE INDEX idx_call_source ON {tn}({col6})'.format(tn=service_calls_table, col6=call_col6))

  for index, call in enumerate(service_calls_csv):
    print("call: " + str(index) + "/" + str(len(service_calls_csv)))
    
    call_date = datetime.datetime.strptime(call[1][:10], "%m/%d/%Y").strftime("%Y%m%d")
    if int(call_date[:4]) > 2017 or int(call_date[:4]) < 2011:
      print("Not processing 2010 or 2018 call - ", call_date)
      continue

    resolution_description = call[21]
    if call_is_duplicate(resolution_description):
      print("  * duplicate complaint found")
      continue

    resolution_violation = resulted_in_violation(call[21])
    resolution_no_action = took_no_action(call[21])
    unresolved = unresolved_call(call[21])

    source = call[3]
    description = call[6]
    building_match = get_building_match(c, call[9])
    if building_match:
      pass
    else: 
      print("  * no building match found")
      continue

    building_id = building_match[0]
    
    # Create call
    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}, {col5}, {col6}, {col7}, {col8}) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'\
      .format(tn=service_calls_table, col1=call_col1, col2=call_col2, col3=call_col3, col4=call_col4, col5=call_col5, col6=call_col6, col7=call_col7, col8=call_col8), (building_id, call_date, description, resolution_description, resolution_violation, resolution_no_action, unresolved, source))

    insertion_id = c.lastrowid

    c.execute('SELECT * FROM {tn} WHERE {cn}={b_id}'\
      .format(tn=buildings_seeds.buildings_table, cn='id', b_id=building_id))

    building = c.fetchone()

    # Create Building Event
    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}, {col4}, {col5}, {col6}) VALUES ({ct_id}, {n_id}, {building_id}, \'{eventable}\', \"{event_id}\", \"{event_date}\")'\
      .format(tn=building_events_seeds.building_events_table, col1="census_tract_id", col2="neighborhood_id", col3="building_id", col4="eventable", col5="eventable_id", col6="event_date", event_date=call_date, ct_id=building[6], n_id=building[7], building_id=building_id, eventable='service_call', event_id=insertion_id))



