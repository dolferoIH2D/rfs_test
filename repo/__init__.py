from repo.settings import default_app_port, DATABASE_URL
from repo.views import AloneRepoView

from tornado.web import Application
from tornado.options import define, options
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from tornado_sqlalchemy import SQLAlchemy

define('port', default=default_app_port, help='Application port')

def main():
    app = Application([
        ('/', AloneRepoView),
    ],
        db = SQLAlchemy(url=DATABASE_URL),
    )
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening on http://localhost:%i' % options.port)
    IOLoop.current().start()
