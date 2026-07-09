#!/usr/bin/env python3
"""Local preview: python3 preview.py [port]  (default 8787)"""
import http.server
import mimetypes
import os
import sys

mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("image/svg+xml", ".svg")


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


os.chdir(os.path.dirname(os.path.abspath(__file__)))
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
print(f"→ http://localhost:{port}/")
http.server.ThreadingHTTPServer(("", port), Handler).serve_forever()
