from http.server import BaseHTTPRequestHandler, HTTPServer
import SQLighter
import json


def convert(data):
    return bytes(json.dumps(data), 'utf-8')


def set_headers(self):
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
    self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")
    self.end_headers()


class HttpProcessor(BaseHTTPRequestHandler):
    data = SQLighter.DB("my.db")

    def do_GET(self):
        segments = self.path.split('/')
        if segments[1] == 'user':
            self.send_response(200)
            set_headers(self)
            self.wfile.write(convert(self.data.get_user(segments[2])))
        if segments[1] == 'master':
            self.send_response(200)
            set_headers(self)
            self.wfile.write(convert(self.data.get_master(segments[2])))
        if segments[1] == 'event':
            self.send_response(200)
            set_headers(self)
            self.wfile.write(convert(self.data.get_event(segments[2])))
        if segments[1] == 'users':
            self.send_response(200)
            set_headers(self)
            self.wfile.write(convert(self.data.get_users()))
        if segments[1] == 'masters':
            self.send_response(200)
            set_headers(self)
            self.wfile.write(convert(self.data.get_masters()))
        if segments[1] == 'events':
            self.send_response(200)
            set_headers(self)
            self.wfile.write(convert(self.data.get_events()))

    def do_DELETE(self):
        segments = self.path.split('/')
        if segments[1] == 'user':
            self.send_response(204)
            set_headers(self)
            self.data.del_user(segments[2])
        if segments[1] == 'master':
            self.send_response(204)
            set_headers(self)
            self.data.del_master(segments[2])
        if segments[1] == 'event':
            self.send_response(204)
            set_headers(self)
            self.data.del_event(segments[2])

    def do_PUT(self):
        length = int(self.headers['content-length'])
        field_data = self.rfile.read(length)
        res_data = json.dumps(field_data.decode('utf-8'))
        segments = self.path.split('/')
        if segments[1] == 'user':
            self.send_response(201)
            set_headers(self)
            self.data.add_user(res_data.email, res_data.name, res_data.surname,
                               res_data.age, res_data.phone)
        if segments[1] == 'master':
            self.send_response(201)
            set_headers(self)
            self.data.add_master(res_data.email, res_data.name, res_data.surname,
                                 res_data.age, res_data.phone, res_data.address, res_data.spec)
        if segments[1] == 'event':
            self.send_response(201)
            set_headers(self)
            self.data.add_event(res_data.user_id, res_data.master_id, res_data.time)

    def do_POST(self):
            length = int(self.headers['content-length'])
            field_data = self.rfile.read(length)
            res_data = json.dumps(field_data.decode('utf-8'))
            segments = self.path.split('/')
            if segments[1] == 'user':
                self.send_response(200)
                set_headers(self)
                self.data.edit_user(res_data.user_id, res_data.email, res_data.name, res_data.surname,
                                                            res_data.age, res_data.phone)
            if segments[1] == 'master':
                self.send_response(200)
                set_headers(self)
                self.data.edit_master(res_data.master_id, res_data.email, res_data.name, res_data.surname,
                                                              res_data.age, res_data.phone, res_data.address,
                                                              res_data.spec)
            if segments[1] == 'event':
                self.send_response(200)
                set_headers(self)
                self.data.edit_event(res_data.event_id, res_data.user_id, res_data.master_id, res_data.time)


if __name__ == '__main__':
    server = HTTPServer(("localhost", 81), HttpProcessor)
    server.serve_forever()

