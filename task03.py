import create-ticket.py
import requests
import json
def GetToken():
    url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    data = {}
    data['username'] = "devnetuser"
    data['password'] = "Cisco123!"
    data= json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data,headers=headers)
    return response.json()

print(GetToken())

import calc
for a in ipcalc.network('192.168.0.1/24'):
    print str(a)
    subnet = ipcalc.Network('255.255.255.0/24')
    print str(subnet.network())
print str(subnet.netmask())
    '192.168.0.1' in Network('192.168.0.1/24')
  def __str__(self):
          ipformat = ""
          for ips in self.ip:
              ipformat = ipformat + str(ips) +  "."

myip = ipaddress([192,168,1,1],[255,255,255,0])

print(myip)

def getTicket():
	url = "https://" + controller + "/api/v1/ticket"


	payload = {"username":"devnetuser","password":"Cisco123!"}


	header = {"content-type": "application/json"}


	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)


	r_json=response.json()


	ticket = r_json["response"]["serviceTicket"]

	return ticket


def getNetworkDevices(ticket):

	url = "https://" + controller + "/api/v1/network-device"


	header = {"content-type": "application/json", "X-Auth-Token":ticket}


	response = requests.get(url, headers=header, verify=False)


	print ("Network Devices = ")
	print (json.dumps(response.json(), indent=4, separators=(',', ': ')))


	r_json=response.json()


	for i in r_json["response"]:
		print(i["id"] + "   " + i["series"])

theTicket=getTicket()
getNetworkDevices(theTicket)
