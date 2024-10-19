from fastapi import FastAPI, HTTPException
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
from config import settings

client = settings.client
write_api = client.write_api(write_options=SYNCHRONOUS)

app = FastAPI(
  title='Telemetry API'
)

@app.get('/set_current_temperature')
def write_sensor_data(serial_number: str, value: float):
  point = Point("sensors").tag("serial_number", serial_number).field("value", value).time(datetime.utcnow())
  # return point.to_line_protocol()
  write_api.write(bucket='home', record=point.to_line_protocol())
  return {'status': 'ok'}

