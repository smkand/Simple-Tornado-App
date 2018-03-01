import os 
import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, testing a torando app")

class AboutHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, testing about page")

class ContactHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, testing contact page")        


def main():
    application = tornado.web.Application([

            (r"/", MainHandler),
            (r"/about", AboutHandler),
            (r"/contact", ContactHandler),
            
        ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()