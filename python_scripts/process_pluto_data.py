import boundary_helpers
import json 
import index_data

from shapely.geometry import mapping, shape, Point

neighborhood_json = {}
with open("data/boundary_data/geojson/bk_neighborhoods.geojson") as neighborhood_data:
  neighborhood_json = json.load(neighborhood_data)
  print("Neighborhood json loaded")

def clean_properties(feature):
  if "SchoolDist" in feature["properties"]:
    del feature["properties"]["SchoolDist"]
  if "FireComp" in feature["properties"]:
    del feature["properties"]["FireComp"]
  if "PolicePrct" in feature["properties"]:
    del feature["properties"]["PolicePrct"]
  if "HealthCent" in feature["properties"]:
    del feature["properties"]["HealthCent"]
  if "HealthArea" in feature["properties"]:
    del feature["properties"]["HealthArea"]
  if "SanitBoro" in feature["properties"]:
    del feature["properties"]["SanitBoro"]
  if "SanitDistr" in feature["properties"]:
    del feature["properties"]["SanitDistr"]
  if "SanitSub" in feature["properties"]:
    del feature["properties"]["SanitSub"]
  if "ZoneDist1" in feature["properties"]:
    del feature["properties"]["ZoneDist1"]
  if "ZoneDist2" in feature["properties"]:
    del feature["properties"]["ZoneDist2"]
  if "ZoneDist3" in feature["properties"]:
    del feature["properties"]["ZoneDist3"]
  if "ZoneDist4" in feature["properties"]:
    del feature["properties"]["ZoneDist4"]
  if "Overlay1" in feature["properties"]:
    del feature["properties"]["Overlay1"]
  if "Overlay1" in feature["properties"]:
    del feature["properties"]["Overlay1"]
  if "Overlay2" in feature["properties"]:
    del feature["properties"]["Overlay2"]
  if "SPDist1" in feature["properties"]:
    del feature["properties"]["SPDist1"]
  if "SPDist2" in feature["properties"]:
    del feature["properties"]["SPDist2"]
  if "SPDist3" in feature["properties"]:
    del feature["properties"]["SPDist3"]
  if "LtdHeight" in feature["properties"]:
    del feature["properties"]["LtdHeight"]
  if "SplitZone" in feature["properties"]:
    del feature["properties"]["SplitZone"]
  if "LandUse" in feature["properties"]:
    del feature["properties"]["LandUse"]
  if "Easements" in feature["properties"]:
    del feature["properties"]["Easements"]
  if "OwnerType" in feature["properties"]:
    del feature["properties"]["OwnerType"]
  if "OwnerName" in feature["properties"]:
    del feature["properties"]["OwnerName"]
  if "LotFront" in feature["properties"]:
    del feature["properties"]["LotFront"]
  if "LotDepth" in feature["properties"]:
    del feature["properties"]["LotDepth"]
  if "BldgFront" in feature["properties"]:
    del feature["properties"]["BldgFront"]
  if "BldgDepth" in feature["properties"]:
    del feature["properties"]["BldgDepth"]
  if "Ext" in feature["properties"]:
    del feature["properties"]["Ext"]
  if "ProxCode" in feature["properties"]:
    del feature["properties"]["ProxCode"]
  if "IrrLotCode" in feature["properties"]:
    del feature["properties"]["IrrLotCode"]
  if "BsmtCode" in feature["properties"]:
    del feature["properties"]["BsmtCode"]
  if "AssessLand" in feature["properties"]:
    del feature["properties"]["AssessLand"]
  if "AssessTot" in feature["properties"]:
    del feature["properties"]["AssessTot"]
  if "ExemptLand" in feature["properties"]:
    del feature["properties"]["ExemptLand"]
  if "ExemptTot" in feature["properties"]:
    del feature["properties"]["ExemptTot"]
  if "YearAlter1" in feature["properties"]:
    del feature["properties"]["YearAlter1"]
  if "YearAlter2" in feature["properties"]:
    del feature["properties"]["YearAlter2"]
  if "HistDist" in feature["properties"]:
    del feature["properties"]["HistDist"]
  if "Landmark" in feature["properties"]:
    del feature["properties"]["Landmark"]
  if "BuiltFAR" in feature["properties"]:
    del feature["properties"]["BuiltFAR"]
  if "ResidFAR" in feature["properties"]:
    del feature["properties"]["ResidFAR"]
  if "CommFAR" in feature["properties"]:
    del feature["properties"]["CommFAR"]
  if "FacilFAR" in feature["properties"]:
    del feature["properties"]["FacilFAR"]
  if "CondoNo" in feature["properties"]:
    del feature["properties"]["CondoNo"]
  if "Sanborn" in feature["properties"]:
    del feature["properties"]["Sanborn"]
  if "TaxMap" in feature["properties"]:
    del feature["properties"]["TaxMap"]
  if "EDesigNum" in feature["properties"]:
    del feature["properties"]["EDesigNum"]
  if "APPBBL" in feature["properties"]:
    del feature["properties"]["APPBBL"]
  if "APPDate" in feature["properties"]:
    del feature["properties"]["APPDate"]
  if "FIRM07_FLA" in feature["properties"]:
    del feature["properties"]["FIRM07_FLA"]
  if "PFIRM15_FL" in feature["properties"]:
    del feature["properties"]["PFIRM15_FL"]
  if "Version" in feature["properties"]:
    del feature["properties"]["Version"]
  if "MAPPLUTO_F" in feature["properties"]:
    del feature["properties"]["MAPPLUTO_F"]
  if "Council" in feature["properties"]:
    del feature["properties"]["Council"]
  if "AreaSource" in feature["properties"]:
    del feature["properties"]["AreaSource"]
  if "CB2010" in feature["properties"]:
    del feature["properties"]["CB2010"]
  if "CD" in feature["properties"]:
    del feature["properties"]["CD"]
  if "ZMCode" in feature["properties"]:
    del feature["properties"]["ZMCode"]
  if "fid" in feature["properties"]:
    del feature["properties"]["fid"]
  if "PLUTOMapID" in feature["properties"]:
    del feature["properties"]["PLUTOMapID"]
  if "RetailArea" in feature["properties"]:
    del feature["properties"]["RetailArea"]
  if "ComArea" in feature["properties"]:
    del feature["properties"]["ComArea"]
  if "FactryArea" in feature["properties"]:
    del feature["properties"]["FactryArea"]
  if "GarageArea" in feature["properties"]:
    del feature["properties"]["GarageArea"]
  if "OfficeArea" in feature["properties"]:
    del feature["properties"]["OfficeArea"]
  if "OtherArea" in feature["properties"]:
    del feature["properties"]["OtherArea"]
  if "StrgeArea" in feature["properties"]:
    del feature["properties"]["StrgeArea"] 
  if "LotType" in feature["properties"]:
    del feature["properties"]["LotType"] 
  if "LotArea" in feature["properties"]:
    del feature["properties"]["LotArea"]
  if "UnitsTotal" in feature["properties"]:
    del feature["properties"]["UnitsTotal"] 
  if "BldgArea" in feature["properties"]:
    del feature["properties"]["BldgArea"] 
  if "ZoneMap" in feature["properties"]:
    del feature["properties"]["ZoneMap"] 
  if "NumBldgs" in feature["properties"]:
    del feature["properties"]["NumBldgs"] 
  if "NumFloors" in feature["properties"]:
    del feature["properties"]["NumFloors"] 
  if "SHAPE_Area" in feature["properties"]:
    del feature["properties"]["SHAPE_Area"] 
  if "SHAPE_Leng" in feature["properties"]:
    del feature["properties"]["SHAPE_Leng"]
  if "XCoord" in feature["properties"]:
    del feature["properties"]["XCoord"] 
  if "YCoord" in feature["properties"]:
    del feature["properties"]["YCoord"]
  if "BBL" in feature["properties"]:
    del feature["properties"]["BBL"] 
  if "ZipCode" in feature["properties"]:
    del feature["properties"]["ZipCode"]
  if "ResArea" in feature["properties"]:
    del feature["properties"]["ResArea"]  

def process_map_pluto():
  with open("data/buildings_data/mappluto.geojson") as file:
    data = json.load(file)
    count = 0
    print(str(len(data["features"])) + str(" features found"))

    new_features = []
    for feature in data["features"]:
      # display count
      count = count + 1
      print(str(count) + "/" + str(len(data["features"])) + " - " + str(len(new_features)) + " included")

      # delete all properties for testing
      # del feature["properties"]

      if feature["properties"]["BldgClass"]:
        if feature["properties"]["UnitsRes"] <= 0:
          continue
        # if(feature["properties"]["BldgClass"][0] != "A" and feature["properties"]["BldgClass"][0] != "B" and feature["properties"]["BldgClass"][0] != "C" and feature["properties"]["BldgClass"][0] != "D" and feature["properties"]["BldgClass"][0] != "L" and feature["properties"]["BldgClass"] != "O8" and feature["properties"]["BldgClass"] != "R0" and feature["properties"]["BldgClass"] != "R1" and feature["properties"]["BldgClass"] != "R2" and feature["properties"]["BldgClass"] != "R3" and feature["properties"]["BldgClass"] != "R4" and feature["properties"]["BldgClass"] != "R5" and feature["properties"]["BldgClass"] != "R6" and feature["properties"]["BldgClass"] != "R7" and feature["properties"]["BldgClass"] != "R8" and feature["properties"]["BldgClass"] != "R9" and feature["properties"]["BldgClass"] != "RR" and feature["properties"]["BldgClass"][0] != "S"):
        #   continue
      else:
        continue

      clean_properties(feature)
      
      # Convert to point
      # if "geometry" in feature:
      #   if feature["geometry"]["type"] != "Point":
      #     polygon = shape(feature["geometry"])
      #     rPoint = polygon.representative_point()
      #     feature["geometry"] = mapping(rPoint)

      #     boundary_helpers.add_neighborhood_property_to_feature(feature, neighborhood_json)

      new_features.append(feature)

    data["features"] = new_features
    
      
    with open("data/buildings_data/processed_mappluto.geojson", "w") as file:
      json.dump(data, file, sort_keys=True, indent=2)


# Clean and process the map pluto data
process_map_pluto()
