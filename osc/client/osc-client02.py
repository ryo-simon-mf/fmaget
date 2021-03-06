import sys
import argparse
import random
import time
import getch
from pythonosc import udp_client


def main():
    arguments = input('Enter Message:')
#   arguments = random.random()
    client.send_message(args.message, arguments)
    print('IP:', args.ip, 'PORT:', args.port, args.message, arguments)
    print('')
#   time.sleep(1)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default = '127.0.0.1', help = 'The IP of the OSC sever')
    parser.add_argument('--port', type = int, default = 2424, help = 'The port of the OSC server is listening on')
    parser.add_argument('--message', default= '/simon', help = 'The message of the OSC server')
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)
   


    try:
        while True:    
            main() 
            
    except KeyboardInterrupt:
        sys.exit(0)
