from sql_alchemy import db

class EntityModel(db.Model):
    __tablename__ = 'entities_scores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    screenName = db.Column(db.String(140))
    score = db.Column(db.Integer)

    def __init__(self, name, screenName, score):
        self.name = name
        self.screenName = screenName
        self.score = score

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'screenName': self.screenName,
            'score': self.score
        }

    @classmethod
    def find_by_id(cls, id):
        entity = cls.query.filter_by(id=id).first()
        if entity:
            return entity
        return None

    @classmethod
    def find(cls, screenName):
        entity = cls.query.filter_by(screenName=screenName).first()
        if entity:
            return entity
        return None

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
