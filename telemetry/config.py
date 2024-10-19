from pydantic_settings import BaseSettings, SettingsConfigDict
from influxdb_client import InfluxDBClient

class Settings(BaseSettings):
  MODE: str

  DB_HOST: str
  DB_TOKEN: str

  LOCAL_DB_HOST: str
  LOCAL_DB_TOKEN: str

  @property
  def client(self):
    if self.MODE == "PROD":
      return InfluxDBClient(url=self.DB_HOST, token=self.DB_TOKEN, org='docs')
    if self.MODE == "LOCAL":
      return InfluxDBClient(url=self.LOCAL_DB_HOST, token=self.LOCAL_DB_TOKEN, org='docs')

  model_config = SettingsConfigDict(env_file=".env")

settings = Settings()