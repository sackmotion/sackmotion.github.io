#!/usr/bin/env python3
import http.server
import sys
from collections import deque

FILE = "hal_log.log"
PORT = 12880 

def tail(filename, n=10):
    with open(filename) as f:
        return deque(f, n)


class TestHandler(http.server.SimpleHTTPRequestHandler):
    """The test example handler."""

    def do_POST(self):
        """Handle a post request by returning the square of the number."""
        print("do_POST")
        #print(self.headers)
        length = int(self.headers.get_all('content-length')[0])
        #print(self.headers.get_all('content-length'))
        data_string = self.rfile.read(length)
        #print(data_string)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        #self.send_header("Access-Control-Allow-Headers", "X-Requested-With, content-type")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.flush_headers()
        deque_text=tail(FILE, int(data_string)) 
        for elem in deque_text:
            self.wfile.write(''.join([elem,'<br/>']).encode())
        
        #self.wfile.write("Here is the response".encode())


    def do_GET(self):
        print("do_GET")
        print(self.headers)   
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.flush_headers() 
        self.wfile.write("404".encode())

def start_server():
    """Start the server."""

    global PORT, FILE
    
    #print (len(sys.argv))
    
    if len(sys.argv) == 2:
        PORT = int(sys.argv[1])
    elif len(sys.argv) == 3:
        PORT = int(sys.argv[1])
        FILE = sys.argv[2]
        
    print("Starting server at port", PORT,"for file", FILE)
    server_address = ("", PORT)
    server = http.server.HTTPServer(server_address, TestHandler)
    server.serve_forever()

start_server()
