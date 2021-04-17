from flask_restful import Resource, reqparse
from entity_model import EntityModel

body_request = reqparse.RequestParser()
body_request.add_argument('name', type=str)
body_request.add_argument('screenName', type=str)
body_request.add_argument('score', type=int)

class Entities(Resource):
    def post(self):
        data = body_request.parse_args()
        screen_name = data.get('screenName')
        
        if EntityModel.find(screen_name):
            return {"message": f"The entity '{screen_name}' already exists."}, 400 # bad request
        entity = EntityModel(**data)
        print('entity',entity.json())
        try:
            entity.save()
            
        except:
            return {'message': 'An internal error ocurred trying to create a new entity.'}, 500
        return entity.json()


class Entity(Resource):
    def get(self, id):
        entity = EntityModel.find_by_id(id)
        if entity:
            return entity.json()
        return {'message': 'Entity not found.'}, 404 # not found

    def delete(self, id):
        entity = EntityModel.find_by_id(id)
        if entity:
            entity.delete()
            return {'message':'Entity deleted.'}
        return {'message': 'Entity not found.'}, 404


class EntityByName(Resource):
    def get(self, screenName):
        entity = EntityModel.find(screenName)
        if entity:
            return entity.json()
        return {'message': 'Entity not found.'}, 404 # not found

    def delete(self, screenName):
        entity = EntityModel.find(screenName)
        if entity:
            entity.delete()
            return {'message':'Entity deleted.'}
        return {'message': 'Entity not found.'}, 404
