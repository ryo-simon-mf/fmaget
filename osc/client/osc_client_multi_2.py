import sys
import argparse
from pythonosc import udp_client

def main():
    arguments = input('Enter Message:')
    
    if arguments == 'FIN':
        print('Finish!!!') 
        sys.exit()

    else:
        for mul in range(args.multi):
            num = str(mul + 1)
            print('IP:', IP_LIST[mul], 'PORT:', args.port, args.message, arguments)
            exec('client{}.send_message(args.message, arguments)'.format(num, IP_LIST[mul]))
        print('')
        return


if __name__ == '__main__':
    IP_LIST = []

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type = int, default = 2424, help = 'The port of the OSC server is listening on')
    parser.add_argument('--multi', type = int, default = 1, help = 'Number of multi client')
    parser.add_argument('--message', default = '/simon', help = 'The message of the OSC server')
    args = parser.parse_args()
    

    for MULTI in range(args.multi):
        num = str(MULTI + 1)

        ip_tmp = input('Enter IP No.' + num + ': ')
        IP_LIST.append(ip_tmp)

        exec('client{} = udp_client.SimpleUDPClient("{}", args.port)'.format(num, ip_tmp))
        print('IP:', IP_LIST[MULTI], 'PORT:', args.port, args.message)

    print(IP_LIST)

    
    while True:    
        main()
    
