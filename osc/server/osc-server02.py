import sys
import argparse
import random
import time
import getch
from pythonosc import osc_server
from pythonosc import dispatcher


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default = '127.0.0.1', help = 'The IP of the OSC sever')
    parser.add_argument('--port', type = int, default = 2424, help = 'The port of the OSC server is listening on')
    parser.add_argument('--message', default= '/simon', help = 'The message of the OSC server')
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map(args.message, print)

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)

    print('IP:', args.ip, 'PORT:', args.port, args.message)
    print('')

    try:
        while True:    
            main()
    except KeyboardInterrupt:
        sys.exit()
        print('End this process')

    server.serve_forever()
