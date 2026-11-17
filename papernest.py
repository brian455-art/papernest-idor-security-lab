"""PaperNest: a localhost-only IDOR teaching application."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys

TOKENS = {
    "alice-demo-token": "Alice",
    "bob-demo-token": "Bob",
}

INVOICES = {
    "inv_A17": {
        "id": "inv_A17",
        "owner": "Alice",
        "description": "Alice test invoice",
        "total": "$12.00",
    },
    "inv_B29": {
        "id": "inv_B29",
        "owner": "Bob",
        "description": "Bob test invoice",
        "total": "$8.00",
    },
}

if len(sys.argv) != 2 or sys.argv[1] not in ("vulnerable", "secure"):
    raise SystemExit("Usage: py papernest.py vulnerable|secure")

MODE = sys.argv[1]


class PaperNestHandler(BaseHTTPRequestHandler):
    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parts = self.path.strip("/").split("/")

        if len(parts) != 2 or parts[0] != "invoice":
            return self.send_json(404, {"error": "Not found"})

        invoice_id = parts[1]
        auth = self.headers.get("Authorization", "")
        pieces = auth.split()

        if len(pieces) != 2 or pieces[0] != "Bearer" or pieces[1] not in TOKENS:
            return self.send_json(401, {"error": "Unauthorized"})

        current_user = TOKENS[pieces[1]]
        invoice = INVOICES.get(invoice_id)

        if invoice is None:
            return self.send_json(404, {"error": "Invoice not found"})

        # The vulnerable version deliberately skips this ownership check.
        if MODE == "secure" and invoice["owner"] != current_user:
            return self.send_json(404, {"error": "Invoice not found"})

        return self.send_json(200, invoice)


print(f"PaperNest ({MODE}) listening at http://127.0.0.1:8765")
print("Press Ctrl+C to stop.")

server = HTTPServer(("127.0.0.1", 8765), PaperNestHandler)
server.serve_forever()
