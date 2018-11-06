"""
Returns the list of unassigned certificates from vManage

Example: python get_unassigned_certificates.py 'vmanage_ip_or_FQDN' 'username' 'password'

PARAMETERS:
    vmanage_ip:     IP address of DNS/FQDN of vManage
    username:       Username used to access vManage
    password:       Password used for Username


"""

import vmanageapi
import json
import sys

def main(args):
    if not len(args) == 3:
        print(__doc__)
        return

    vmanage_ip, username, password = args[0], args[1], args[2]
    api_call = 'certificate/vedge/list'

    response = vmanageapi.main([vmanage_ip, username, password, api_call])

    d = json.loads(response)

    for x in range(len(d['data'])):
        if d['data'][x]['vedgeCertificateState'] == 'tokengenerated':
            print(x, d['data'][x]['serialNumber'], d['data'][x]['chasisNumber'])


if __name__ == '__main__':
    main(sys.argv[1:])
    sys.exit()
