from pydantic import BaseModel
from typing import Optional

class SDevice(BaseModel):
  serial_number: str
  status: Optional[bool] = False
class SChangeDevice(BaseModel):
  serial_number: str
  status: bool

