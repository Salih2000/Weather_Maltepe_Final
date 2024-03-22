# kafka_consumer.py
from kafka import KafkaConsumer
import json

def consume_from_kafka(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092', group_id='my-group')
    for message in consumer:
        yield json.loads(message.value.decode('utf-8'))
