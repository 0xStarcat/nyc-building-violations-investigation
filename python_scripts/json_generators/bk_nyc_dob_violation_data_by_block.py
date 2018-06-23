import os,sys,inspect
sys.path.insert(1, os.path.join(sys.path[0], '..')) 

import index_data

index_data.index_by_key("data/violations_data/json/processed_bk_violation_data_2008_2017.json", "data/violations_data/json/bk_nyc_dob_violation_data_by_block_2008_2017.json", "block")