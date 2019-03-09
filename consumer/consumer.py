from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('spider_eis_fz44', bootstrap_servers='stable-kafka-1:9092', auto_offset_reset='latest')

for msg in consumer:
    val = json.load(msg.val)
    print(val)

