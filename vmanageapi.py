"""
Class with REST Api GET and POST libraries

MODIFIED: Taken directly from https://sdwan-docs.cisco.com/Product_Documentation/Command_Reference/vManage_REST_APIs/vManage_REST_APIs_Overview/Using_the_vManage_REST_APIs

Example: python vmanageapi.py vmanage_hostname username password [api_call]

PARAMETERS:
    vmanage_hostname : Ip address of the vmanage or the dns name of the vmanage
    username : Username to login the vmanage
    password : Password to login the vmanage
    api_call : the api call to query

Note: The first three arguments are manadatory.  The api_call is 'certificate/vedge/list'
      if not specified on the CLI or call
"""
import requests
import sys
import json

if 'InsecureRequestWarning' in dir(requests.packages.urllib3.exceptions):
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class rest_api_lib:
    def __init__(self, vmanage_ip, username, password):
        self.vmanage_ip = vmanage_ip
        self.session = {}
        self.login(self.vmanage_ip, username, password)

    def login(self, vmanage_ip, username, password):
        """Login to vmanage"""
        base_url_str = 'https://%s/'%vmanage_ip

        login_action = '/j_security_check'

        #Format data for loginForm
        login_data = {'j_username' : username, 'j_password' : password}

        #Url for posting login data
        login_url = base_url_str + login_action

        url = base_url_str + login_url

        sess = requests.session()

        #If the vmanage has a certificate signed by a trusted authority change verify to True
        login_response = sess.post(url=login_url, data=login_data, verify=False)

        # if '<html>' in login_response.content:
        #     print("Login Failed")
        #     sys.exit(0)

        self.session[vmanage_ip] = sess

    def get_request(self, mount_point):
        """GET request"""
        url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, mount_point)
        ## print(url)
        response = self.session[self.vmanage_ip].get(url, verify=False)
        data = response.content
        return data

    def post_request(self, mount_point, payload, headers={'Content-Type': 'application/json'}):
        """POST request"""
        url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, mount_point)
        payload = json.dumps(payload)
        response = self.session[self.vmanage_ip].post(url=url, data=payload, headers=headers, verify=False)
        data = response.content

def main(args):
    if not len(args) >= 3:
        print(__doc__)
        return
    vmanage_ip, username, password = args[0], args[1], args[2]
    obj = rest_api_lib(vmanage_ip, username, password)
    #Example request to get devices from the vmanage "url=https://vmanage.viptela.com/dataservice/device"
    if len(args) >= 4:
        api_call = args[3]
    else:
        api_call = 'certificate/vedge/list'

    # print('api_call:', api_call)

    response = obj.get_request(api_call)
    ## print(response)
    #Example request to make a Post call to the vmanage "url=https://vmanage.viptela.com/dataservice/device/action/rediscover"
    # payload = {"action":"rediscover","devices":[{"deviceIP":"172.16.248.105"},{"deviceIP":"172.16.248.106"}]}
    # response = obj.post_request('device/action/rediscover', payload)
    # print(response)

    return(response)

if __name__ == "__main__":
    response=main(sys.argv[1:])
    print(response)
    sys.exit()

