from confluent_kafka import Producer

def send_to_kafka(topic, data):
    config = {
        'bootstrap.servers': 'localhost:9092', 
    }

    producer = Producer(config)
    producer.produce(topic, data)
    producer.flush()
