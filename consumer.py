
import json
from kafka import KafkaConsumer

TOPIC = "campus-sensors"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="tp05-campus-monitor",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)
#total_temperature = 0
#event_count = 0
print(f"Listening to topic: {TOPIC}")

try:
    for message in consumer:

        event = message.value
        #if event["campus_building"] != "Building A":
        # continue
        temperature = event["temperature_c"]
       # event_count += 1
        #total_temperature += temperature

        #average = total_temperature / event_count

        print(
            f'{event["timestamp"]} | {event["sensor_id"]} | '
            f'T={temperature}°C | RH={event["humidity_pct"]}%'
        )

        if temperature >= 35:
            print("ALERT: High temperature detected!")

except KeyboardInterrupt:
    print("Consumer stopped by user.")

finally:
    consumer.close()

#python3 consumer.py