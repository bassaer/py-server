from http.server import SimpleHTTPRequestHandler, HTTPServer
from socket import gethostbyname, gethostname


class Handler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"hello":"world"}')


def main():
    host = gethostbyname(gethostname())
    port = 8000
    with HTTPServer(('', port), Handler) as httpd:
        print('serving ==> {}:{}'.format(host, port))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
