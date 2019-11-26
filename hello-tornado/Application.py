import tornado.web
import tornado.ioloop


class LoginHandle(tornado.web.RequestHandler):
    def get(self):
        return self.write(r'<h1>hello,tornado</h1>')

    def post(self):
        name = self.get_argument('name')
        return self.write(f'name is :{name}')


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        return self.write(f'<h1>hello{self.get_argument("name")}')


def post(self):
    name = self.get_argument('name')
    return self.write(f'name is :{name}')


def main():
    app = tornado.web.Application(
        handlers=[(r'/login', LoginHandle), (r'/hello', HelloHandler)],
        cookie_secret='MWM2MzEyOWFlOWRiOWM2MGMzZThhYTk0ZDNlMDA0OTU='
    )
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
