table = 'buildings'

col1 = 'total_violations'
col2 = 'total_sales'

def add_columns(c):

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col1))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col2))

def migrate_buildings_data(c):
  # add_columns(c)

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