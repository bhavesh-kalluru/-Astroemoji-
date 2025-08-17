from datetime import datetime
from .db import db

class Constellation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(16), unique=True, index=True, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    text = db.Column(db.Text, nullable=False)
    emojis = db.Column(db.String(64), nullable=True)
    seed = db.Column(db.String(64), nullable=False)
    data_json = db.Column(db.Text, nullable=False)  # serialized JSON
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Constellation {self.slug} '{self.title}'>"
