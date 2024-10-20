from fastapi import FastAPI, HTTPException
from schemas.SDevice import SDevice, SChangeDevice
from schemas.SSensor import SSensor
from schemas.STargetTemperature import STargetTemperature
from repositories.Managment import Managment
from controllers.Command import consume
from aiokafka import AIOKafkaConsumer
import asyncio

app = FastAPI(
  title='Device Managment'
)

@app.on_event("startup")
async def startup_event():
    # Запускаем consumer в фоновом режиме
    asyncio.create_task(consume())

@app.post('/add_device')
async def add_device(device: SDevice):
  existing_device = await Managment.find_device_by_serial_number(device.serial_number)
  if existing_device:
    raise HTTPException(status_code=400, detail="device is already registered")
  response = await Managment.add_device(device.model_dump())
  target_temperature = STargetTemperature(device_id=device.serial_number, temperature=18)
  await set_target_temperature(target_temperature)
  return True

@app.get('/status_device')
async def status_device(serial_number: str):
  device = await Managment.find_device_by_serial_number(serial_number)
  return device

@app.put('/change_device_status')
async def change_device_status(device: SChangeDevice):
  response = await Managment.update_device(device.model_dump())
  return response

@app.post('/add_sensor')
async def add_sensor(sensor: SSensor):
  existing_sensor = await Managment.find_sensor_by_serial_number(sensor.serial_number)
  if existing_sensor:
    raise HTTPException(status_code=400, detail="sensor is already registered")
  response = await Managment.add_sensor(sensor.model_dump())
  return True

@app.get('/get_target_temperature')
async def get_target_temperature(device_id: str):
  response = await Managment.find_target_temperature_by_device_id(device_id)
  return response['temperature']

@app.put('/set_target_temperature')
async def set_target_temperature(target_temperature: STargetTemperature):
  existing_target_temperature = await Managment.find_target_temperature_by_device_id(target_temperature.device_id)
  if existing_target_temperature:
    response = await Managment.update_target_temperature(target_temperature.model_dump())
  else:
    response = await Managment.add_target_temperature(target_temperature.model_dump())
  return response

