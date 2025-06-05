import http.server
import socketserver
from urllib.parse import urlparse

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Only log requests for image files, ignoring query strings
        path = urlparse(self.path).path.lower()
        if path.endswith(('.png', '.jpg', '.jpeg', '.webp')):
            print(f"[Image Loaded] {path}")

PORT = 7861
with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
    print(f"Serving silently on port {PORT}")
    httpd.serve_forever()
