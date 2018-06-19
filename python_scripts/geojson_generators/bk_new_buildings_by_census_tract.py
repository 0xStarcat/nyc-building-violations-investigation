import index_data

def generate_geojson():
    index_data.index_by_key("data/buildings_data/geojson/bk_new_buildings.geojson", "data/buildings_data/geojson/bk_new_buildings_by_census_tract.geojson", "CT2010")