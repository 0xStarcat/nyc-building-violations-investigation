import count_features_by_key

def generate_csv():
  count_features_by_key.count_by_key("data/buildings_data/processed_mappluto.geojson", "data/buildings_data/csv/bk_buildings_by_census_tract_totals.csv", "CT2010")
