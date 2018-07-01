table = 'neighborhoods'

col1 = 'total_buildings'
col2 = 'total_violations'
col3 = 'total_sales'
col4 = 'total_permits'
col5 = 'total_sales_prior_violations'
col6 = 'avg_violation_count_3years_before_sale'
col7 = 'total_service_calls'
col8 = 'total_service_calls_with_violation_result'

def add_columns(c):
  # c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
  #   .format(tn=table, cn=col1))

  # c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
  #   .format(tn=table, cn=col2))

  # c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
  #   .format(tn=table, cn=col3))

  # c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
  #   .format(tn=table, cn=col4))

  # c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
  #   .format(tn=table, cn=col5))

  # c.execute("ALTER TABLE {tn} ADD COLUMN {cn} REAL"\
  #   .format(tn=table, cn=col6))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col7))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col8))

def migrate_neighborhoods_data(c):
  # add_columns(c)

  c.execute('SELECT * FROM {tn}'\
    .format(tn=table))
  
  results = c.fetchall()
  
  for index, row in enumerate(results):
    print("updating row " + str(index) + '/' + str(len(results)))

    # Buildings
    c.execute('SELECT * FROM buildings WHERE neighborhood_id={id}'\
      .format(id=row[0]))

    buildings_count = len(c.fetchall())
    print(buildings_count)

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col1, value=buildings_count, id=row[0]))

    # Violations
    c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND neighborhood_id={id}'\
      .format(event='violation', id=row[0]))

    violations_count = len(c.fetchall())

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col2, value=violations_count, id=row[0]))

    # sales

    c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND neighborhood_id={id}'\
      .format(event='sale', id=row[0]))

    sales_count = len(c.fetchall())

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col3, value=sales_count, id=row[0]))

    # permits

    c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND neighborhood_id={id}'\
      .format(event='permit', id=row[0]))

    permits_count = len(c.fetchall())

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col4, value=permits_count, id=row[0]))

    # service calls

    c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND neighborhood_id={id}'\
      .format(event='service_call', id=row[0]))

    service_calls = c.fetchall()
    service_calls_count = len(service_calls)

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col7, value=service_calls_count, id=row[0]))

    # service calls with violation result
    
    service_calls_violation_result_count = 0

    for event in service_calls:
      c.execute('SELECT * FROM service_calls WHERE id={id}'.format(id=event[5]))
      if c.fetchone()[5] == True:
        service_calls_violation_result_count += 1

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col8, value=service_calls_violation_result_count, id=row[0]))

    # Sales w Prior Violations
    # Average violation count in 3 years prior to sale
    sales_with_priors = []
    prior_violations_count = 0
    c.execute('SELECT * FROM buildings WHERE neighborhood_id={id}'\
      .format(id=row[0]))

    buildings = c.fetchall()

    for building_row in buildings:
      c.execute('SELECT * FROM sales WHERE building_id={id}'\
        .format(id=building_row[0]))

      sales = c.fetchall()

      for sales_row in sales:
        sale_date = sales_row[2]
        sale_year = sale_date[:4]
        three_years_ago = str(int(sale_year) - 3) + sale_date[4:]

        c.execute('SELECT * FROM violations WHERE issue_date < \'{sale_date}\' AND issue_date > \'{three_years_ago}\' AND building_id={id} '\
          .format(id=building_row[0], sale_date=sales_row[2], three_years_ago=three_years_ago))

        violations = c.fetchall()
        prior_violations_count += len(violations)
        if len(violations) > 0:
          sales_with_priors.append(sales_row)
        else:
          continue

    print(len(sales_with_priors))

    avg_violation_count_before_sale = round(prior_violations_count / len(sales_with_priors), 2) if prior_violations_count else 0
    print(prior_violations_count)
    print(avg_violation_count_before_sale)
    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col5, value=len(sales_with_priors), id=row[0]))
    

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col6, value=avg_violation_count_before_sale, id=row[0]))

