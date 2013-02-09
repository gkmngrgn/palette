import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

from urls import handlers
from settings import settings, option_list


class Application(tornado.web.Application):
    def __init__(self):
        """
        Application class of the project. We define handlers, configuration,
        database connection and more..
        """
        # define options
        for option in option_list:
            name = option.pop('name')
            define(name, **option)

        tornado.web.Application.__init__(self, handlers, **settings)


def runserver():
    """
    Runs tornado web server.
    """
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    runserver()
