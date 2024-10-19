from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
from config import settings

# Создаем клиент InfluxDB
client = settings.client

# Создаем API для записи данных
write_api = client.write_api(write_options=SYNCHRONOUS)

def write_sensor_data(serial_number: str, value: float):
    point = Point("sensors").tag("serial_number", serial_number).field("value", value).time(datetime.utcnow())
    write_api.write(bucket='home', record=point)

def close_client():
    client.close()