
import json
import csv
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "campus-sensors",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="tp05-csv-group",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)

with open("sensor_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "event_id",
        "sensor_id",
        "temperature_c",
        "humidity_pct",
        "timestamp"
    ])

    print("Saving events to CSV...")

    try:
        for message in consumer:
            event = message.value

            writer.writerow([
                event["event_id"],
                event["sensor_id"],
                event["temperature_c"],
                event["humidity_pct"],
                event["timestamp"]
            ])

            file.flush()
            print("Saved:", event["event_id"])

    except KeyboardInterrupt:
        print("CSV consumer stopped.")

    finally:
        consumer.close()
#python3 consumer_csv.py