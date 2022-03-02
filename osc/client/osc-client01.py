import argparse
import random
import time

from pythonosc import udp_client

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default = '127.0.0.1', help = 'The IP of the OSC sever')
    parser.add_argument('--port', type = int, default = 2424, help = 'The port of the OSC server is listening on')
    parser.add_argument('--message', default= '/simon', help = 'The message of the OSC server')
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    for x in range(10):
        
        arguments = random.random()

        client.send_message(args.message, arguments)
        print(args.message, arguments)
        time.sleep(1)
