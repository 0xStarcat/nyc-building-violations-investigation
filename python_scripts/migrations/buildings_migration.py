table = 'buildings'

col1 = 'total_violations'
col2 = 'total_sales'
col3 = 'total_service_calls'
col4 = 'total_service_calls_with_violation_result'
col5 = 'total_service_calls_with_no_action_result'
col6 = 'total_service_calls_unresolved_result'

def add_columns(c):

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col1))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col2))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col3))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col4))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col5))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col6))

def migrate_buildings_data(c):
  add_columns(c)

  c.execute('SELECT * FROM {tn}'\
    .format(tn=table))

  results = c.fetchall()

  for index, row in enumerate(results):
    print("updating row " + str(index) + '/' + str(len(results)))

    # Violations
    c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND building_id={id}'\
      .format(event='violation', id=row[0]))

    violations_count = len(c.fetchall())

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col1, value=violations_count, id=row[0]))

    # sales

    c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND building_id={id}'\
      .format(event='sale', id=row[0]))

    sales_count = len(c.fetchall())

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col2, value=sales_count, id=row[0]))

    # service calls

    c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND building_id={id}'\
      .format(event='service_call', id=row[0]))

    service_calls = c.fetchall()
    service_calls_count = len(service_calls)

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col3, value=service_calls_count, id=row[0]))

    # service calls with result
    
    service_calls_violation_result_count = 0
    service_calls_no_action_result_count = 0
    service_calls_unresolved_result_count = 0

    for event in service_calls:
      c.execute('SELECT * FROM service_calls WHERE id={id}'.format(id=event[5]))
      entry = c.fetchone()
      if entry[5] == True:
        service_calls_violation_result_count += 1
      elif entry[6] == True:
        service_calls_no_action_result_count += 1
      elif entry[7] == True:
        service_calls_unresolved_result_count += 1

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col4, value=service_calls_violation_result_count, id=row[0]))
    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col5, value=service_calls_no_action_result_count, id=row[0]))
    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col6, value=service_calls_unresolved_result_count, id=row[0]))

    print(service_calls_count, service_calls_violation_result_count, service_calls_no_action_result_count, service_calls_unresolved_result_count)