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
import getpass

def get_credentials():
    username = input('Please enter a vManage username: ')
    password = getpass.getpass(prompt='Please enter the password for ' + username + ': ')

    return(username, password)


def main(args):

    if len(args) == 3:
        vmanage_ip, username, password = args[0], args[1], args[2]
    elif len(args) == 1:
        vmanage_ip = args[0]
        username, password = get_credentials()
    else:
        vmanage_ip = input('Please enter vManage IP address: ')
        username, password = get_credentials()


    api_call = 'certificate/vedge/list'

    response = vmanageapi.main([vmanage_ip, username, password, api_call])

    d = json.loads(response)

    if len(d['data']) > 0:
        print('{: >2}: {: <35} {: <35}'.format('#', 'Token', 'Chassis #'))

        for x in range(len(d['data'])):
            if d['data'][x]['vedgeCertificateState'] == 'tokengenerated':
                print('{: >2}: {: <35} {: <35}'.format(x, d['data'][x]['serialNumber'], d['data'][x]['chasisNumber']))

    else:
        print('No available certificates found')

    print()


if __name__ == '__main__':
    main(sys.argv[1:])
    sys.exit()
