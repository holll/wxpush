import tornado.ioloop
import tornado.web

import handler

application = tornado.web.Application([
    (r'/send', handler.SendmsgHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
