from http.server import BaseHTTPRequestHandler, HTTPServer


class WebRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health/":
            self.send_response(200)
        else:
            self.send_response(404)
        self.send_header("Content-Type", "text/text")
        self.end_headers()
        self.wfile.write("".encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()
