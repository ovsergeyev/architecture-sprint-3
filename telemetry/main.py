from fastapi import FastAPI, HTTPException
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS
from aiokafka import AIOKafkaProducer
import asyncio
from datetime import datetime
from config import settings
from schemas.STemperature import STemperature
import json

client = settings.client
write_api = client.write_api(write_options=SYNCHRONOUS)

producer = None

app = FastAPI(
  title='Telemetry API'
)

@app.on_event("startup")
async def startup_event():
  global producer
  producer = AIOKafkaProducer(bootstrap_servers=settings.kafka_address)
  await producer.start()

@app.on_event("shutdown")
async def shutdown_event():
  await producer.stop()

@app.post('/set_current_temperature')
async def write_sensor_data(temperature: STemperature):
  point = Point("sensors").tag("serial_number", temperature.serial_number).field("value", temperature.value).time(datetime.utcnow())
  write_api.write(bucket='home', record=point.to_line_protocol())

  await producer.send_and_wait(settings.topic, temperature.model_dump_json().encode('utf-8'))
  return True

@app.get('/last_temperature')
def get_last_temperature(serial_number: str):
    query = f'''
    from(bucket: "home")
      |> range(start: -1h)  // Здесь вы можете изменить диапазон по необходимости
      |> filter(fn: (r) => r["_measurement"] == "sensors" and r["serial_number"] == "{serial_number}")
      |> last()
    '''

    result = client.query_api().query(org='docs', query=query)

    if result:
        for table in result:
            for record in table.records:
                return {
                    'serial_number': serial_number,
                    'value': record.get_value(),
                    'time': record.get_time()
                }

    return {'status': 'not found'}

