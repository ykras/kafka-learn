from kafka import KafkaProducer
import datetime

producer = KafkaProducer(bootstrap_servers='stable-kafka-1:9092')
for _ in range(1000000):
    producer.send('kafka-learn', bytes("i'm trying hard at {}!!!".format(datetime.datetime.now()), 'utf-8'))

producer.flush()
producer.close(timeout=60)