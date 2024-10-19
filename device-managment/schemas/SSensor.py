from pydantic import BaseModel
from typing import Optional

class SSensor(BaseModel):
  serial_number: str
  device_id: str

