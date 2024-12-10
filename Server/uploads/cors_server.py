from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path.endswith('.json'):
            with open(parsed_path.path[1:], 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(file.read())
        else:
            SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print(f'Serving HTTP on port {server_address[1]}...')
    httpd.serve_forever()