from fastapi import FastAPI, HTTPException
from schemas.SDevice import SDevice, SChangeDevice
from schemas.STargetTemperature import STargetTemperature
from repositories.Managment import Managment

app = FastAPI(
  title='Device Managment'
)

@app.post('/add_device')
async def add_device(device: SDevice):
  existing_device = await Managment.find_device_by_serial_number(device.serial_number)
  if existing_device:
    raise HTTPException(status_code=400, detail="device is already registered")
  response = await Managment.add_device(device.model_dump())
  target_temperature = STargetTemperature(device_id=device.serial_number, temperature=18)
  await set_target_temperature(target_temperature)
  return response

@app.get('/status_device')
async def status_device(serial_number: str):
  device = await Managment.find_device_by_serial_number(serial_number)
  return device.status

@app.put('/change_device_status')
async def change_device_status(device: SChangeDevice):
  response = await Managment.update_device(device.model_dump())
  return response

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

