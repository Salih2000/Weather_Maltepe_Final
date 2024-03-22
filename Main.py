import time
import json
import logging
from Fetch_Weather_data import get_location_key, get_current_weather
from Produce_To_Kafka import send_to_kafka
from Consume_From_Kafka import consume_from_kafka
from Insert_To_Mssql import write_to_mssql

logging.basicConfig(level=logging.INFO)

api_key = "Write your api key here"
city_name = "Maltepe"

def main():
    interval_seconds = 10
    topic = 'Weather_Maltepe'

    while True:
        logging.info("Fetching location key...")
        location_key = get_location_key(api_key, city_name)
        if location_key:
            logging.info("Location key found: %s", location_key)
            logging.info("Getting current weather...")
            weather_data = get_current_weather(api_key, location_key)
            if weather_data:
                logging.info("Current weather data retrieved: %s", weather_data)
                logging.info("Sending weather data to Kafka...")
                send_to_kafka(topic, json.dumps(weather_data))
                
                logging.info("Consuming weather data from Kafka...")
                for data in consume_from_kafka(topic):
                    logging.info("Consumed weather data: %s", data)
                    logging.info("Writing weather data to MSSQL...")
                    write_to_mssql(data)
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()
