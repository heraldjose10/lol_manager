from api import db


class Champion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    q = db.Column(db.String(128))
    w = db.Column(db.String(128))
    e = db.Column(db.String(128))
    r = db.Column(db.String(128))
    store_price = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f'<Champion {self.id} {self.name}>'
