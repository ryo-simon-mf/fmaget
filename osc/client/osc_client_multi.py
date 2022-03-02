import sys
import argparse
import random
import time
import getch
from pythonosc import udp_client

def main():
    arguments = input('Enter Message:')
    
    if arguments == 'FIN':
        print('Finish!!!') 
        sys.exit()
    else:
        for mul in range(args.multi):
            print('IP:', IP_LIST[mul], 'PORT:', args.port, args.message, arguments)
#           client.send_message(IP_LIST[mul], arguments)
            exec('client{}.send_message(IP_LIST[mul],arguments)'.format(str(mul + 1)))
        print('')
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type = int, default = 2424, help = 'The port of the OSC server is listening on')
    parser.add_argument('--multi', type = int, default = 1, help = 'Number of multi client')
    parser.add_argument('--message', default = '/simon', help = 'The message of the OSC server')
    args = parser.parse_args()
    
    IP_NUM = []
    IP_LIST = []

    for MULTI in range(args.multi):
        ip_tmp = input('Enter IP No.' + str(MULTI + 1) + ': ')
        IP_LIST.append(ip_tmp)
        exec('client{} = udp_client.SimpleUDPClient("{}", args.port)'.format(str(MULTI + 1), str(IP_LIST[MULTI])))
        print('IP:', IP_LIST[MULTI], 'PORT:', args.port, args.message)

    print(IP_LIST)

    
    while True:    
        main()
    
