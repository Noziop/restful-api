#!/usr/bin/python3
''' Module that implements a simple API '''


from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json


# Constants
CONTENT_TYPE_JSON = 'application/json'
CONTENT_TYPE_TEXT = 'text/plain'


class Handler(BaseHTTPRequestHandler):
    ''' Handler for HTTP requests '''

    routes = {
        '/': ('Hello, this is a simple API!', CONTENT_TYPE_TEXT),
        '/data': ({
            "name": "John",
            "age": 30,
            "city": "New York"
            }, CONTENT_TYPE_JSON),
        '/info': ({
            "version": "1.0",
            "description": "A simple API built with http.server"
            }, CONTENT_TYPE_JSON),
        '/status': ({"status": "OK"}, CONTENT_TYPE_JSON)
    }

    def do_GET(self):
        ''' Handles GET requests '''
        parsed_path = urlparse(self.path)
        route = self.routes.get(parsed_path.path)

        if route:
            content, content_type = route
            self.send_response_content(content, content_type)
        else:
            self.send_error_response(404, "Endpoint not found")

    def send_response_content(self, content, content_type):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        if isinstance(content, str):
            self.wfile.write(content.encode())
        else:
            self.wfile.write(json.dumps(content).encode())

    def send_error_response(self, status_code, message):
        self.send_response(status_code)
        self.send_header('Content-type', CONTENT_TYPE_TEXT)
        self.end_headers()
        self.wfile.write(message.encode())


def run(server_class=HTTPServer, handler_class=Handler, port=8000):
    ''' Starts the HTTP server '''
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
