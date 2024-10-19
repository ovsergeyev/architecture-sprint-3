from pydantic import BaseModel
from typing import Optional

class STargetTemperature(BaseModel):
  device_id: str
  temperature: float

