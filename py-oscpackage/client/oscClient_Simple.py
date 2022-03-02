import sys
import argparse
from pythonosc import udp_client

def main():
    arguments = input('Enter Message:')
    
    if arguments == 'FIN':
        print('Finish!!!') 
        sys.exit()
    else:
        client.send_message(args.message, arguments)

        print('')
        print('IP:', args.ip, 'PORT:', args.port, args.message, arguments)
        print('')
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default = '127.0.0.1', help = 'The IP of the OSC sever')
    parser.add_argument('--port', type = int, default = 8000, help = 'The port of the OSC server is listening on')
    parser.add_argument('--message', default = '/default', help = 'The message of the OSC server')
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    
    print('IP:', args.ip, 'PORT:', args.port, args.message)
    print('')

    while True:    
        main()
    
