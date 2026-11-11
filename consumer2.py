
import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "campus-sensors",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="tp05-second-group",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)

print("Second consumer group is listening...")

try:
    for message in consumer:
        print("Received:", message.value)

except KeyboardInterrupt:
    print("Consumer stopped.")

finally:
    consumer.close()
