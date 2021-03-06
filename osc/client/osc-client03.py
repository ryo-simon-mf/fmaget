import sys
import argparse
import random
import time
import getch
from pythonosc import udp_client


#def exit():
#    print('If you keep sending, press any button.')
#    key = ord(getch.getch())
#    if key == 27:
#        print('           Finish this program')
#        sys.exit()
#    else:
#        pass
#    return

def main():
    arguments = input('Enter Message:')
    
    if arguments == 'FIN':
        sys.exit()
    else:
    
        client.send_message(args.message, arguments)
        print('IP:', args.ip, 'PORT:', args.port, args.message, arguments)
        print('')
#        exit()
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default = '127.0.0.1', help = 'The IP of the OSC sever')
    parser.add_argument('--port', type = int, default = 2424, help = 'The port of the OSC server is listening on')
    parser.add_argument('--message', default= '/simon', help = 'The message of the OSC server')
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    
    print('IP:', args.ip, 'PORT:', args.port, args.message)

    while True:    
        main()
    
