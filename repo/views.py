import json

from repo.settings import rsa_size
from repo.models import User
from repo.utils import generate_rsa_pair

from tornado.web import RequestHandler
from tornado.gen import coroutine

from tornado_sqlalchemy import SessionMixin, as_future


class AloneRepoView(RequestHandler, SessionMixin):
    """
    Our lone view of test project.
    It takes username by get and returns public_key. If there is no username
    in db or no associated with username key, then we create record in db and
    return created public key.
    """
    SUPPORTED_METHODS = ['GET']

    def send_response(self, data, status=200):
        self.set_status(status)
        self.write(data)

    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json; charset="utf-8"')

    @coroutine
    def get(self):
        username = self.get_argument('username', None)
        if username:
            print('Got request for username <%s>' % username)
            # Get key for user or create record in db
            with self.make_session() as session:
                user = yield as_future(session.query(User).filter(
                    User.username==username
                ).first)
                if not user:
                    keys = generate_rsa_pair(rsa_size)
                    user = User(
                        username = username,
                        public_key = keys.get('public_key'),
                    )
                    session.add(user)
                self.send_response(
                    {
                        'username': user.username,
                        'publick_key': str(user.public_key),
                    },
                    status=201,
                )
        else:
            self.send_response('No username provided', status=400)
