import buildings_seeds
import census_tracts_seeds
import neighborhoods_seeds

building_events_table = 'building_events'

def seed_building_events(c):
  print("Seeding Building Events...")
  event_col1 = 'census_tract_id'
  event_col2 = 'neighborhood_id'
  event_col3 = 'building_id'
  event_col4 = 'eventable'
  event_col5 = 'eventable_id'


  c.execute('CREATE TABLE IF NOT EXISTS {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {col1} INTEGER NOT NULL REFERENCES {ct_table}(id), {col2} INTEGER NOT NULL REFERENCES {n_table}(id), {col3} INTEGER NOT NULL REFERENCES {bldg_table}(id), {col4} TEXT NOT NULL, {col5} INTEGER NOT NULL)'\
    .format(tn=building_events_table, col1=event_col1, col2=event_col2, col3=event_col3, col4=event_col4, col5=event_col5, ct_table=census_tracts_seeds.census_tracts_table, n_table=neighborhoods_seeds.neighborhoods_table, bldg_table=buildings_seeds.buildings_table))

  c.execute('CREATE INDEX idx_census_tract_building_events ON {tn}({col1})'.format(tn=building_events_table, col1=event_col1))
  c.execute('CREATE INDEX idx_neighborhood_building_events ON {tn}({col1})'.format(tn=building_events_table, col1=event_col2))
  c.execute('CREATE INDEX idx_building_building_events ON {tn}({col1})'.format(tn=building_events_table, col1=event_col3))

  