import boundary_helpers
import json 
import index_data
import count_features_by_boundary
import count_features_by_key
import census_tract_helpers

from csv_generators import bk_census_tract_median_income

# Neighorhoods

# boundary_helpers.add_neighborhood_to_census_tract()

# Tracts
# bk_census_tract_median_income.generate_csv()
# boundary_helpers.add_median_income_to_census_tracts()

# boundary_helpers.process_files_new_buildings_by_year_and_total()

census_tract_helpers.write_csv_violations_per_building_per_year()
boundary_helpers.add_computed_violation_data_to_census_tracts()