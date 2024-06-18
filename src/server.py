from http.server import HTTPServer, SimpleHTTPRequestHandler

def run_preview_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Live preview server running at http://localhost:8000")
    httpd.serve_forever()
