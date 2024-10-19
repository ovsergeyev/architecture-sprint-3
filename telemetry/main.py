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

@app.get('/latest_temperature')
def get_latest_temperature(serial_number: str):
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

