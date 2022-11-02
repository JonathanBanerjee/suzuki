#!/usr/bin/env python3
# Python 3 Server
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys
import logging

start = time.time()
current = time.ctime() 

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        logging.basicConfig(filname='helloworld.py',
        encoding='utf-8', level=logging.DEBUG)
        if self.send_response ==200:
            logging.info(f'Page Obtained at:{current}')
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Hello World!</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Hello World!.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        if time.time() - start > 60:
           sys.exit(1)


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
