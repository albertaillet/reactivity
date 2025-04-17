#!/usr/bin/env python3
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

HOST, PORT = "localhost", 8000


class StaticAndAPIHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if urlparse(self.path).path != "/api/my-endpoint":
            self.send_error(404)
            return
        if self.headers.get("Content-Type") != "application/json":
            self.send_error(415, "Unsupported Media Type")
            return
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
            return
        try:
            username = payload["username"]
            quantity = int(payload["quantity"])
            comments = payload["comments"]
            tags = payload["tags"]
        except KeyError as e:
            self.send_error(400, f"Missing field: {e}")
            return
        except ValueError:
            self.send_error(400, "Invalid value type")
            return

        # "Business logic"
        response = {
            "greeting": f"Hello, {username}!",
            "processedQuantity": quantity,
            "echoedComments": comments,
            "normalizedTags": [
                t.strip().lower() for t in tags if isinstance(t, str)
            ],
        }
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

if __name__ == "__main__":
    print(f"Serving files and simple API on http://{HOST}:{PORT}/")
    HTTPServer((HOST, PORT), StaticAndAPIHandler).serve_forever()
