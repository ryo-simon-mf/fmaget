import sys
import argparse
from pythonosc import udp_client 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default = '127.0.0.1', help = 'The IP of the OSC server')
    parser.add_argument('--port', type =  int, default = 8000, help = 'The port of the OSC server is listening on')
    parser.add_argument('--message', default = '/default', help = 'The message of the OSC server')
    parser.add_argument('--sent', default = 'HelloWorld', help = 'The sent text to the OSC server')
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)
    client.send_message(args.message, args.sent)


if __name__ == '__main__':
    main()
