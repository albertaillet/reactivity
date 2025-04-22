#!/usr/bin/env python3
import json
import os
import pathlib
import sqlite3
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
            search = payload.get("search")
            max_rows = min(int(payload["maxRows"]), 20)
        except Exception:
            self.send_error(400, "Invalid payload")
            return
        if search is None or not isinstance(search, str):
            self.send_error(400, "Invalid payload")
            return
        cur = con.cursor()
        query = "SELECT id, Title FROM recipes WHERE Instructions LIKE ? LIMIT ?"
        cur.execute(query, (f"%{search}%", max_rows))
        rows = cur.fetchall()
        response = [{"id": row[0], "title": row[1]} for row in rows]
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))


if __name__ == "__main__":
    repo_path = pathlib.Path(__file__).parent
    con = sqlite3.connect(repo_path / "database.db")
    print(f"Serving files and simple API on http://{HOST}:{PORT}/")
    os.chdir(repo_path / "static")  # Change to the static directory
    HTTPServer((HOST, PORT), StaticAndAPIHandler).serve_forever()
