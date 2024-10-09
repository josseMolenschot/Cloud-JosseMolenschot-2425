####  DELETE WEBEX "DEMO" SPACES
from webexteamssdk import WebexTeamsAPI
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
access_token = "ZjhkODRjNWMtMDJlMy00N2JlLThkMjEtYTgxNWMyZDkwMGViY2FhMzYyMGQtNDcw_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de"
api = WebexTeamsAPI(access_token=access_token)
# Find all rooms that should be removed
all_rooms = api.rooms.list()

demo_rooms = [room for room in all_rooms if 'GROUP_JMO_' in room.title]

# Delete all of the demo rooms
for room in demo_rooms:
    print("Deleting ... " + room.title)
    api.rooms.delete(room.id)