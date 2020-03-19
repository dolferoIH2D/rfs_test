from repo.settings import DATABASE_URL

from sqlalchemy import Column, String, BigInteger
from tornado_sqlalchemy import SQLAlchemy

db = SQLAlchemy(url=DATABASE_URL)

class User(db.Model):
    """
        Model stores User object with only 3 fields:
        id, username, public_key
    """
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    username = Column(String, unique=True)
    public_key = Column(String)

    def __repr__(self):
        return "<USER(username='%s, public_key=%s')" % (self.username, self.public_key)
