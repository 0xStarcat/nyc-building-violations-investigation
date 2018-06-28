table = 'census_tracts'

col1 = 'total_buildings'
col2 = 'total_violations'
col3 = 'total_sales'
col4 = 'total_permits'

def add_columns(c):

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col1))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col2))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col3))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col4))

def migrate_census_tracts_data(c):
  # add_columns(c)

  c.execute('SELECT * FROM {tn}'\
    .format(tn=table))
  
  results = c.fetchall()
  
  for index, row in enumerate(results):
    print("updating row " + str(index) + '/' + str(len(results)))

    # Buildings
    c.execute('SELECT * FROM buildings WHERE census_tract_id={id}'\
      .format(id=row[0]))

    buildings_count = len(c.fetchall())
    print(buildings_count)

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col1, value=buildings_count, id=row[0]))

    # Violations
    c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND census_tract_id={id}'\
      .format(event='violation', id=row[0]))

    violations_count = len(c.fetchall())

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col2, value=violations_count, id=row[0]))

    # sales

    c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND census_tract_id={id}'\
      .format(event='sale', id=row[0]))

    sales_count = len(c.fetchall())

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col3, value=sales_count, id=row[0]))

    # permits

    c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND census_tract_id={id}'\
      .format(event='permit', id=row[0]))

    permits_count = len(c.fetchall())

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col4, value=permits_count, id=row[0]))

