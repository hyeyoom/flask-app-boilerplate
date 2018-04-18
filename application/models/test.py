"""mock models"""
from application.index import db

class MockMockMock(db.Model):
    __tablename__ = 'mockmock'
    id = db.Column(db.Integer, db.Sequence('mockmockmock_id_seq'), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __repr__(self) -> str:
        return "<MockMockMock('%s', '%s)>" % (self.email, self.password)
