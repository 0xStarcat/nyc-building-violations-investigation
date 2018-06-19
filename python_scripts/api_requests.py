# https://data.cityofnewyork.us/Housing-Development/DOB-Violations/3h2n-5cm9
# https://data.cityofnewyork.us/Housing-Development/DOB-ECB-Violations/6bgk-3dad
# https://dev.socrata.com/docs/queries/where.html

import requests
import json
import boundary_helpers
# Boro = 3 (brooklyn)
# Issued between dates
# violation_type_code is not
  # "c" (construction), 
  # "LL5" or "LL5/83" (fire safety in office buildings), 
  # "ES" (electric sign, probably business)
all_data = []

dob_url = 'https://data.cityofnewyork.us/resource/dvnq-fhaa.json?boro=3&$where=issue_date between "20120101" and "20171231" AND violation_type_code not in("E", "LL5", "LL5/73", "ES")&'

# violation_type is not "Site Safety, Elevator"
  # "OPERATION OF A PLACE OF ASSEMBLY W/O A CURRENT CERTIFICATE OF OCCUANCY.OBSERED:A78 SEAT CHURCH W. SOUND SYSTEM AND MUSICAL INSTRUMENTS FOR ALIVE BEND @EXTENSION @REAR OF FIRST FLR, W/O A CURRENT CERTIFICATE OF" was filed under "Construction"
ecb_url = 'https://data.cityofnewyork.us/resource/gq3f-5jm8.json?boro=3&$where=issue_date between "20120101" and "20171231" AND violation_type not in("Site Safety", "Elevators")&'

def request_from_api(url):
  print(url)
  offset = 0
  limit = 50000
  request_data = []
  

  def request(off):
    r = requests.get(url+'$limit='+str(limit)+'&$offset=' + str(off))

    request_data = json.loads(r.text)
    for d in request_data:
      all_data.append(d)
    
    return request_data

  while len(request(offset)) > 0:
    offset = offset + limit

    print(len(all_data))

request_from_api(dob_url)
request_from_api(ecb_url)  

with open("data/violations_data/nyc_dob_data.json", "w") as dob_json:
  print(str(len(all_data)) + " total records found") 
  json.dump(all_data, dob_json, sort_keys=True, indent=2)

