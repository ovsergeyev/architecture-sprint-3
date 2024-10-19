from fastapi import FastAPI, HTTPException

app = FastAPI(
  title='Telemetry API'
)

@app.get('/test')
async def add_device():
  return 'this is test'

