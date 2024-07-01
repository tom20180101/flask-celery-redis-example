from db import db
from sqlalchemy import and_,or_,between
class Hot(db.Model):
    __tablename__ = 'hot'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    detail_id = db.Column(db.Integer,nullable=False)
    view_count = db.Column(db.Integer,nullable=False)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        db.session.close()





