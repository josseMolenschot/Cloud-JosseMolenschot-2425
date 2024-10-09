import requests 
import json 
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
access_token = "ZjhkODRjNWMtMDJlMy00N2JlLThkMjEtYTgxNWMyZDkwMGViY2FhMzYyMGQtNDcw_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de"

groups_struc = {
 "groups": [
      { "group": { "group_id": "G1" , "group_name": "GROUP_JMO_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Josse", "email": "josse.molenschot@student.odisee.be"},
                     {"person_id": "P-2" , "person_name": "Yvan", "email": "yvan.rooseleer@biasc.be"}
                   ]
                 }
      },
      { "group": { "group_id": "G2" , "group_name": "GROUP_JMO_B" ,    
                   "members": [   
                     #{"person_id": "P-4" ,"person_name": "Martin", "email": "martin@biasc.be"}, 
                     #{"person_id": "P-5" ,"person_name": "Bob", "email": "bob@biasc.be"}, 
                     #{"person_id": "P-6" ,"person_name": "Alice", "email": "alice@biasc.be"} 
                   ]     
                 }
      }
   ]
}

url = 'https://api.ciscospark.com/v1/rooms'

headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["group_name"]
    print("Creating ... " + create_group_name)
    payload_space={"title": create_group_name}
    res_space = requests.post(url, headers=headers, json=payload_space)

    NEW_SPACE_ID = res_space.json()["id"]
    for mbr in rec["group"]["members"]:
        room_id = NEW_SPACE_ID
        person_email = mbr["email"] 
        url2 = 'https://api.ciscospark.com/v1/memberships'
        payload_member = {'roomId': room_id, 'personEmail': person_email}
        res_member = requests.post(url2, headers=headers, json=payload_member)
