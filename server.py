import requests
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/stats":
            data = requests.get("https://www.kickstarter.com/projects/wearefictional/reroll-visual-character-sheet-app-for-5e-dnd/stats.json?v=1").content
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(data)
            fileHandler = open('./data.txt', 'a')
            fileHandler.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + data.decode("utf-8"))
            fileHandler.close()
        else:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(Path("./client.html").read_bytes())


server = HTTPServer(('', 9000), Handler)
server.serve_forever()