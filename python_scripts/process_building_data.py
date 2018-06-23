import index_data
import count_features_by_key

from csv_generators import bk_buildings_by_census_tract_totals_generator
from csv_generators import bk_buildings_by_neighborhood_totals_generator

# Index Blocks
index_data.index_by_key("data/buildings_data/processed_mappluto.geojson", "data/buildings_data/json/bk_buildings_by_block.json", "Block")

# Index neighborhoods
# index_data.index_by_key("data/buildings_data/processed_mappluto.geojson", "data/buildings_data/json/bk_buildings_by_neighborhood.json", "neighborhood")

# Index census tracts
# index_data.index_by_key("data/buildings_data/processed_mappluto.geojson", "data/buildings_data/json/bk_buildings_by_census_tract.json", "CT2010")

# Count buildings by neighborhood
# count_features_by_key.count_by_key("data/buildings_data/processed_mappluto.geojson", "data/buildings_data/csv/bk_buildings_by_neighborhood_totals.csv", "neighborhood")
# bk_buildings_by_neighborhood_totals_generator.generate_csv()

# Count buildings by census_tract
# bk_buildings_by_census_tract_totals_generator.generate_csv()
