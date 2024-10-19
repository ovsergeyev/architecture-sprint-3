from pydantic_settings import BaseSettings, SettingsConfigDict
from influxdb_client import InfluxDBClient

class Settings(BaseSettings):
  MODE: str

  DB_HOST: str
  DB_PORT: int
  DB_TOKEN: str
  DB_ORG: str

  LOCAL_DB_HOST: str
  LOCAL_DB_PORT: int
  LOCAL_DB_TOKEN: str
  LOCAL_DB_ORG: str

  @property
  def client(self):
    if self.MODE == "PROD":
      return InfluxDBClient(url=f"http://{self.DB_HOST}:{self.DB_PORT}", token=self.DB_TOKEN, org=self.DB_ORG)
    if self.MODE == "LOCAL":
      return InfluxDBClient(url=f"http://{self.LOCAL_DB_HOST}:{self.LOCAL_DB_PORT}", token=self.LOCAL_DB_TOKEN, org=self.LOCAL_DB_ORG)

  model_config = SettingsConfigDict(env_file=".env")

settings = Settings()