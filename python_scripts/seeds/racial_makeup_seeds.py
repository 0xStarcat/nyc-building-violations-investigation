racial_makeup_table = 'racial_makeups'

def seed_racial_makeups(c, racial_makeup_csv):
  print("Seeding racial_makeups...")
  race_col1 = 'sub_borough_name'
  race_col2 = 'percent_white_2011'
  race_col3 = 'percent_white_2016'

  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} TEXT, {col2} REAL, {col3} REAL)'\
    .format(tn=racial_makeup_table, col1=race_col1, col2=race_col2, col3=race_col3))

  for row in racial_makeup_csv:
    c.execute('INSERT OR IGNORE INTO {tn} ({col1}, {col2}, {col3}) VALUES (?, ?, ?)'\
      .format(tn=racial_makeup_table, col1=race_col1, col2=race_col2, col3=race_col3), (row[2], float(row[10]), float(row[15])))