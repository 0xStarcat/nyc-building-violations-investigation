table = 'neighborhoods'

col1 = 'total_buildings'
col2 = 'total_violations'
col3 = 'total_sales'
col4 = 'total_permits'
col5 = 'total_sales_prior_violations'
col6 = 'avg_violation_count_3years_before_sale'
col7 = 'total_service_calls'
col8 = 'total_service_calls_with_violation_result'
col9 = 'total_service_calls_with_no_action_result'
col10 = 'total_service_calls_unresolved_result'
col11 = 'racial_makeup_id'

def find_racial_makeup(c, neighborhood):
  c.execute('SELECT * FROM racial_makeups')

  n_name = neighborhood[1]
  racial_makeups = c.fetchall()
  for row in racial_makeups:
    print(row[1])
    if row[1] == "Williamsburg/Greenpoint":
      if n_name == "Williamsburg" or n_name == "Greenpoint":
        return row[0]
    elif row[1] == "Brooklyn Heights/Fort Greene":
      if n_name == "Brooklyn Heights" or n_name == "Fort Greene" or n_name == "Cobble Hill" or n_name == "DUMBO" or n_name == "Vinegar Hill" or n_name == "Navy Yard" or n_name == "Boerum Hill" or n_name == "Clinton Hill" or n_name == "Downtown Brooklyn":
        return row[0]
    elif row[1] == "Bedford Stuyvesant":
      if n_name == "Bedford-Stuyvesant":
        return row[0]
    elif row[1] == "Bushwick":
      if n_name == "Bushwick":
        return row[0]
    elif row[1] == "East New York/Starrett City":
      if n_name == "East New York" or n_name == "Cypress Hills":
        return row[0]
    elif row[1] == "Park Slope/Carroll Gardens":
      if n_name == "Park Slope" or n_name == "Carroll Gardens" or n_name == "Red Hook"  or n_name == "Columbia St" or n_name == "Gowanus" or n_name == "South Slope" or n_name == "Prospect Park":
        return row[0]
    elif row[1] == "Sunset Park":
      if n_name == "Sunset Park" or n_name == "Windsor Terrace" or n_name == "Green-Wood Cemetery":
        return row[0]
    elif row[1] == "North Crown Heights/Prospect Heights":
      if n_name == "Prospect Heights" or n_name == "Crown Heights":
        return row[0]
    elif row[1] == "South Crown Heights":
      if n_name == "Prospect-Lefferts Gardens":
        return row[0]
    elif row[1] == "Bay Ridge":
      if n_name == "Bay Ridge" or n_name == "Fort Hamilton" or n_name == "Dyker Heights":
        return row[0]
    elif row[1] == "Bensonhurst":
      if n_name == "Bensonhurst" or n_name == "Bath Beach":
        return row[0]
    elif row[1] == "Borough Park":
      if n_name == "Borough Park" or n_name == "Kensington":
        return row[0]
    elif row[1] == "Coney Island":
      if n_name == "Coney Island" or n_name == "Sea Gate" or n_name == "Brighton Beach":
        return row[0]
    elif row[1] == "Flatbush":
      if n_name == "Flatbush" or n_name == "Midwood":
        return row[0]
    elif row[1] == "Sheepshead Bay/Gravesend":
      if n_name == "Sheepshead Bay" or n_name == "Gravesend" or n_name == "Manhattan Beach" or n_name == "Gerritsen Beach" or n_name == "Marine Park":
        return row[0]
    elif row[1] == "Brownsville/Ocean Hill":
      if n_name == "Brownsville":
        return row[0]
    elif row[1] == "East Flatbush":
      if n_name == "East Flatbush":
        return row[0]
    elif row[1] == "Flatlands/Canarsie":
      if n_name == "Flatlands" or n_name == "Canarsie" or n_name == "Plum Beach" or n_name == "Floyd Bennett Field" or n_name == "Mill Basin" or n_name == "Bergen Beach" or n_name == "Jamaica Bay":
        return row[0]
    else:
      print("  * unable to match", n_name)
      return False

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

  # c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
  #   .format(tn=table, cn=col7))

  # c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
  #   .format(tn=table, cn=col8))

  # c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
  #   .format(tn=table, cn=col9))

  # c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
  #   .format(tn=table, cn=col10))

  c.execute("ALTER TABLE {tn} ADD COLUMN {cn} INT"\
    .format(tn=table, cn=col11))

def migrate_neighborhoods_data(c):
  # add_columns(c)

  c.execute('SELECT * FROM {tn}'\
    .format(tn=table))
  
  results = c.fetchall()
  
  for index, row in enumerate(results):
    print("updating row " + str(index) + '/' + str(len(results)))

    # # Buildings
    # c.execute('SELECT * FROM buildings WHERE neighborhood_id={id}'\
    #   .format(id=row[0]))

    # buildings_count = len(c.fetchall())
    # print(buildings_count)

    # c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
    #   .format(tn=table, cn=col1, value=buildings_count, id=row[0]))

    # # Violations
    # c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND neighborhood_id={id}'\
    #   .format(event='violation', id=row[0]))

    # violations_count = len(c.fetchall())

    # c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
    #   .format(tn=table, cn=col2, value=violations_count, id=row[0]))

    # # sales

    # c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND neighborhood_id={id}'\
    #   .format(event='sale', id=row[0]))

    # sales_count = len(c.fetchall())

    # c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
    #   .format(tn=table, cn=col3, value=sales_count, id=row[0]))

    # # permits

    # c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND neighborhood_id={id}'\
    #   .format(event='permit', id=row[0]))

    # permits_count = len(c.fetchall())

    # c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
    #   .format(tn=table, cn=col4, value=permits_count, id=row[0]))

    # # service calls

    # c.execute('SELECT * FROM building_events WHERE eventable=\'{event}\' AND neighborhood_id={id}'\
    #   .format(event='service_call', id=row[0]))

    # service_calls = c.fetchall()
    # service_calls_count = len(service_calls)

    # c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
    #   .format(tn=table, cn=col7, value=service_calls_count, id=row[0]))

    # # service calls with result
    
    # service_calls_violation_result_count = 0
    # service_calls_no_action_result_count = 0
    # service_calls_unresolved_result_count = 0

    # for event in service_calls:
    #   c.execute('SELECT * FROM service_calls WHERE id={id}'.format(id=event[5]))
    #   entry = c.fetchone()
    #   if entry[5] == True:
    #     service_calls_violation_result_count += 1
    #   elif entry[6] == True:
    #     service_calls_no_action_result_count += 1
    #   elif entry[7] == True:
    #     service_calls_unresolved_result_count += 1

    # c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
    #   .format(tn=table, cn=col8, value=service_calls_violation_result_count, id=row[0]))
    # c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
    #   .format(tn=table, cn=col9, value=service_calls_no_action_result_count, id=row[0]))
    # c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
    #   .format(tn=table, cn=col10, value=service_calls_unresolved_result_count, id=row[0]))

    # print(service_calls_count, service_calls_violation_result_count, service_calls_no_action_result_count, service_calls_unresolved_result_count)

    # # Sales w Prior Violations
    # # Average violation count in 3 years prior to sale
    # sales_with_priors = []
    # prior_violations_count = 0
    # c.execute('SELECT * FROM buildings WHERE neighborhood_id={id}'\
    #   .format(id=row[0]))

    # buildings = c.fetchall()

    # for building_row in buildings:
    #   c.execute('SELECT * FROM sales WHERE building_id={id}'\
    #     .format(id=building_row[0]))

    #   sales = c.fetchall()

    #   for sales_row in sales:
    #     sale_date = sales_row[2]
    #     sale_year = sale_date[:4]
    #     three_years_ago = str(int(sale_year) - 3) + sale_date[4:]

    #     c.execute('SELECT * FROM violations WHERE issue_date < \'{sale_date}\' AND issue_date > \'{three_years_ago}\' AND building_id={id} '\
    #       .format(id=building_row[0], sale_date=sales_row[2], three_years_ago=three_years_ago))

    #     violations = c.fetchall()
    #     prior_violations_count += len(violations)
    #     if len(violations) > 0:
    #       sales_with_priors.append(sales_row)
    #     else:
    #       continue

    # print(len(sales_with_priors))

    # avg_violation_count_before_sale = round(prior_violations_count / len(sales_with_priors), 2) if prior_violations_count else 0
    # print(prior_violations_count)
    # print(avg_violation_count_before_sale)
    # c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
    #   .format(tn=table, cn=col5, value=len(sales_with_priors), id=row[0]))
    

    # c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
    #   .format(tn=table, cn=col6, value=avg_violation_count_before_sale, id=row[0]))

    # racial makeups

    c.execute('UPDATE {tn} SET {cn} = {value} WHERE id={id}'\
      .format(tn=table, cn=col11, value=find_racial_makeup(c, row), id=row[0]))
