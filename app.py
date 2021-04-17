from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from entity_resource import Entity, Entities, EntityByName

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///score.db'
api = Api(app)

@app.route('/')
def index():
    return '<h1>Up and running...</h1>'

api.add_resource(Entities, '/entities')
api.add_resource(Entity, '/entities/<int:id>/score')
api.add_resource(EntityByName, '/entities/<string:screenName>/score')

def create_app():
    from sql_alchemy import db
    db.init_app(app)
    return app

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(host="0.0.0.0", port=8000, debug=True)