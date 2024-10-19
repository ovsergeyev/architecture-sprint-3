from pydantic_settings import BaseSettings, SettingsConfigDict
from influxdb_client import InfluxDBClient

class Settings(BaseSettings):
  MODE: str

  DB_HOST: str
  DB_PORT: int
  DB_TOKEN: str
  DB_ORG: str

  KAFKA_HOST: str
  KAFKA_PORT: int
  KAFKA_TOPIC: str

  LOCAL_DB_HOST: str
  LOCAL_DB_PORT: int
  LOCAL_DB_TOKEN: str
  LOCAL_DB_ORG: str

  LOCAL_KAFKA_HOST: str
  LOCAL_KAFKA_PORT: int
  LOCAL_KAFKA_TOPIC: str

  @property
  def client(self):
    if self.MODE == "PROD":
      return InfluxDBClient(url=f"http://{self.DB_HOST}:{self.DB_PORT}", token=self.DB_TOKEN, org=self.DB_ORG)
    if self.MODE == "LOCAL":
      return InfluxDBClient(url=f"http://{self.LOCAL_DB_HOST}:{self.LOCAL_DB_PORT}", token=self.LOCAL_DB_TOKEN, org=self.LOCAL_DB_ORG)

  @property
  def topic(self):
    if self.MODE == "PROD":
      return self.KAFKA_TOPIC
    if self.MODE == "LOCAL":
      return self.LOCAL_KAFKA_TOPIC

  @property
  def kafka_address(self):
    if self.MODE == "PROD":
      return f"{self.KAFKA_HOST}:{self.KAFKA_PORT}"
    if self.MODE == "LOCAL":
      return f"{self.LOCAL_KAFKA_HOST}:{self.LOCAL_KAFKA_PORT}"

  model_config = SettingsConfigDict(env_file=".env")

settings = Settings()