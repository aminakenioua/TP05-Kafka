
# TP05 - Real-Time Data Streaming Using Apache Kafka

## Student Information
University: University of Eloued
Faculty: Faculty of Exact Sciences
Department: Computer Science
Master: Artificial Intelligence and Data Science
Module: Big Data Analytics
Academic Year: 2026/2027

## Project Description
This project implements a real-time sensor monitoring system using Apache Kafka and Python.

The system generates temperature and humidity readings and streams them through Kafka.

## Technologies
- Apache Kafka 3.9.1
- Docker Compose
- Python
- kafka-python
- JSON

## Project Structure
tp05-kafka/
- compose.yaml
- requirements.txt
- producer.py
- consumer.py
- consumer2.py
- consumer_csv.py
- README.md
- screenshots/

## How to Run

### 1. Start Kafka
docker compose up -d

### 2. Activate Python Environment
source .venv/bin/activate

### 3. Install Dependencies
python -m pip install -r requirements.txt

### 4. Run Consumer
python consumer.py

### 5. Run Producer
python producer.py

## Additional Tasks
- Send 100 events.
- Calculate running average temperature.
- Create a second consumer group.
- Change topic partitions.
- Add campus_building field.
- Export events to CSV.

## Conclusion
This practical work demonstrates how Apache Kafka supports real-time data streaming and processing using Python.

