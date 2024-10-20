from pydantic import BaseModel
from typing import Optional

class STemperature(BaseModel):
  serial_number: str
  value: float

