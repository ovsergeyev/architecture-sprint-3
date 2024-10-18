from fastapi import FastAPI, APIRouter

app = FastAPI(
  title='Device Managment'
)

@app.post('/add_device')
async def add_device():
  return "add device"

@app.get('/status_device')
async def status_device():
  return "status device"

@app.put('/set_target_temperature')
async def set_target_temperature():
  return "set temperature"

@app.put('/change_device_status')
async def change_device_status():
  return "change status device"

