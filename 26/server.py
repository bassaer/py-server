from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from socket import gethostbyname, gethostname


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write('{"hello":"world"}')

def main():
    host = gethostbyname(gethostname())
    port = 8000
    httpd = HTTPServer(('', port), Handler)
    print('serving ==> {0}:{1}'.format(host, port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()



if __name__ == '__main__':
    main()
