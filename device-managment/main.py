from fastapi import FastAPI, APIRouter
from schemas.SDevice import SDevice, SChangeDevice
from schemas.STargetTemperature import STargetTemperature
from repositories.Managment import Managment

app = FastAPI(
  title='Device Managment'
)

@app.post('/add_device')
async def add_device(device: SDevice):
  response = await Managment.add_device(device.model_dump())
  return device

@app.get('/status_device')
async def status_device(serial_number: str):
  device = await Managment.find_device(serial_number = serial_number)
  return device.status

@app.put('/change_device_status')
async def change_device_status(device: SChangeDevice):
  response = await Managment.update_device_by_serial_number(device.model_dump())
  return response

@app.put('/set_target_temperature')
async def set_target_temperature(data: STargetTemperature):
  response = await Managment.add_target_temperature(data.model_dump())
  return response

