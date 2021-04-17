import pika
import json
from app import create_app
from entity_model import EntityModel
from config_json import AMQPS

app = create_app()

params = pika.URLParameters(AMQPS)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='friends')


def callback(ch, method, properties, body):
    
    data = json.loads(body)
    print(data)

    if properties.content_type == 'friend_added':
        with app.app_context():
            entity = EntityModel.find_by_id(data.get('entity_id'))
            entity.score += 1
            entity.save()
            print(entity.json())
            print('stakeholder receives += 1')
        

    if properties.content_type == 'friend_deleted':
        with app.app_context():
            entity = EntityModel.find_by_id(data.get('entity_id'))
            entity.score -= 1
            entity.save()
            print(entity.json())
            print('stakeholder receives -= 1')


channel.basic_consume(queue='friends', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()