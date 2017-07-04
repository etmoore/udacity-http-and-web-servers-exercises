#!/usr/bin/env python3
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
# .send_header and end_headers are methods on the parent class, BaseHTTPRequestHandler

        # Now, write the response body.
        self.wfile.write("Hello, HTTP!\n".encode())

if __name__ == '__main__': # If the file is being run as the "main" program...
    server_address = ('', 8000)  # Serve on all addresses, port 8000. The right side of the assignment statement contains a "tuple"
    httpd = HTTPServer(server_address, HelloHandler) # httpd for daemon? This is an instance of the HTTPServer class. We've handed it our handler class.
    httpd.serve_forever()
