import socketserver
from http.server import BaseHTTPRequestHandler
import SQLighter


def req():
    ...


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path() == '':
            req()

        self.send_response(200)


if __name__ == '__main__':
    data = SQLighter.DB("my.db")
    data.afk("users", {
        "name": "text",
        "id": "number",
        "role": "text"
    }, "id")
    httpd = socketserver.TCPServer(('', 8080), MyHandler)
    httpd.serve_forever()

