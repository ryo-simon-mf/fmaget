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
            print('IP:', IP_LIST[mul], 'PORT:', PORT_LIST[mul], MESSAGE_LIST[mul], arguments)
            exec('client{}.send_message("{}", arguments)'.format(num, MESSAGE_LIST[mul]))
        print('')
        return


if __name__ == '__main__':
    IP_LIST = []
    PORT_LIST = []
    MESSAGE_LIST = []
    parser = argparse.ArgumentParser()
    parser.add_argument('--multi', type = int, default = 1, help = 'Number of multi client')
    args = parser.parse_args()
    

    for MULTI in range(args.multi):
        num = str(MULTI + 1)

        ip_tmp = input('Enter IP No.' + num + ': ')
        port_tmp = input('Enter PORT No.' + num + ': ')
        message_tmp = input('Enter MESSAGE No.' + num + ': ')
        IP_LIST.append(ip_tmp)
        PORT_LIST.append(port_tmp)
        MESSAGE_LIST.append(message_tmp)

        exec('client{} = udp_client.SimpleUDPClient("{}", int({}))'.format(num, ip_tmp, port_tmp))
        print('IP:', IP_LIST[MULTI], 'PORT:', PORT_LIST[MULTI], MESSAGE_LIST[MULTI])

    while True:    
        main()
    
