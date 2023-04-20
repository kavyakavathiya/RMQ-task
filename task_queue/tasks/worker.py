import pika
import time
import json
from pymongo import MongoClient

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')

def callback(ch, method, properties, body):
    task = json.loads(body)['task']
    print(f'Received task: {task}')

    # process task
    client = MongoClient('mongodb://db:27017/')
    db = client['task_queue']
    collection = db['tasks']
    collection.insert_one({'task': task})
    time.sleep(5) # simulate processing time

    print(f'Finished task: {task}')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
