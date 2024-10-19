from fastapi import FastAPI, HTTPException
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from config import settings
from datetime import datetime

client = settings.client
write_api = client.write_api(write_options=SYNCHRONOUS)

app = FastAPI(
  title='Telemetry API'
)

@app.get('/test')
def write_sensor_data(serial_number: str, value: float):
    point = Point("sensors").tag("serial_number", serial_number).field("value", value).time(datetime.utcnow())
    write_api.write(bucket='home', record=point)

