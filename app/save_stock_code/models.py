from app import app
from app import db
from app import ma

class CorrespoondenceTable(db.Model):
    __tablename__ = 'correspoondence_table'

    code = db.Column(db.String(10), primary_key = True)
    name = db.Column(db.String(10))

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __repr__(self):
        return 'name %s' %self.name

class CorrespoondenceTableSchema(ma.Schema):
    class Meta:
        fields = (
            "code",
            "name"
        )