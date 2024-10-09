import requests
import json
import datetime
requests.packages.urllib3.disable_warnings()

print ("Current date and time: ")
print (datetime.datetime.now())
print ('Starting DNA Center Hello World - Simple')
print ('Creating Hard Coded Variables')

DNAC_scheme = 'https://'
DNAC_authority = 'sandboxdnac.cisco.com'
DNAC_port = ':443'
DNAC_path_token = '/dna/system/api/v1/auth/token'
DNAC_path = '/dna/intent/api/v1/network-device'
DNAC_user = 'devnetuser'
DNAC_psw = 'Cisco123!'
#WDNAC_user = input("Username? ")
#DNAC_psw = input("Password? ")

token_req_url = DNAC_scheme+DNAC_authority+DNAC_path_token
print (token_req_url)
auth = (DNAC_user, DNAC_psw)
print (type(auth))

req = requests.post(token_req_url, auth=auth, verify=False)
print (dir(req))
print ("API Return Code: " + str(req.status_code))
print ('Request URI: ' + token_req_url)
print ("Username: " + DNAC_user)
resp = req.text
print (resp)
token = req.json()["Token"]
print ("Recieved Token:")
print (token)
print ("Length Token:")
print (len(token))

print ('Inventory Request - Network Devices')

req_url = DNAC_scheme+DNAC_authority+DNAC_path
print (req_url)
header_data = {'X-auth-token': token}
resp_devices = requests.request('GET', req_url, headers=header_data, verify=False)
print (resp_devices)
resp_devices_json = resp_devices.json()
print('-----------------------------------')

dev_dict = json.loads(resp_devices.text)
print (dev_dict["response"][0].keys())
print ('----------------------------------')
print ("Response (json):")
print (json.dumps(resp_devices_json, indent=2))


import os
import json
import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_file

# Initialize the Flask app
app = Flask(__name__)

# Sample JSON response with devices (replace this with actual response)
json_data = dev_dict

# Function to create and save the network map as an image
def create_network_map():
    G = nx.Graph()

    # Parse the JSON response and add nodes and edges
    for device in json_data['response']:
        hostname = device['hostname']
        ip = device['managementIpAddress']
        mac = device['macAddress']

        # Add node for each switch
        G.add_node(hostname, ip=ip, mac=mac)

        # Create an edge between all devices (example: fully connected)
        for other_device in json_data['response']:
            if other_device != device:
                G.add_edge(hostname, other_device['hostname'])

    # Draw the network graph
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')

    # Add IP labels
    ip_labels = {device['hostname']: device['managementIpAddress'] for device in json_data['response']}
    nx.draw_networkx_labels(G, pos, labels=ip_labels, font_color='red', font_size=8, verticalalignment='bottom')

    # Save the graph to an image file
    img_path = 'DNAC_API_TEST/static/network_map.png'
    plt.savefig(img_path)
    plt.close()

    return img_path

@app.route('/')
def home():
    # Generate the network map image
    img_path = create_network_map()

    # Get the table data from JSON
    devices = json_data['response']

    # Render the home page with the table and network map
    return render_template('home.html', devices=devices, image_path=img_path)

# Serve the network map image
@app.route('/static/<path:filename>')
def static_file(filename):
    return send_file(os.path.join('static', filename))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

