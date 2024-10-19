from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  MODE: str

  DB_HOST: str
  DB_PORT: int
  DB_USER: str
  DB_PASS: str
  DB_NAME: str

  LOCAL_DB_HOST: str
  LOCAL_DB_PORT: int
  LOCAL_DB_USER: str
  LOCAL_DB_PASS: str
  LOCAL_DB_NAME: str

  KAFKA_HOST: str
  KAFKA_PORT: int
  KAFKA_TOPIC: str

  LOCAL_KAFKA_HOST: str
  LOCAL_KAFKA_PORT: int
  LOCAL_KAFKA_TOPIC: str

  @property
  def DATABASE_URL(self):
    if self.MODE == "PROD":
      print(f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
      return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    if self.MODE == "LOCAL":
      print(f"postgresql+asyncpg://{self.LOCAL_DB_USER}:{self.LOCAL_DB_PASS}@{self.LOCAL_DB_HOST}:{self.LOCAL_DB_PORT}/{self.LOCAL_DB_NAME}")
      return f"postgresql+asyncpg://{self.LOCAL_DB_USER}:{self.LOCAL_DB_PASS}@{self.LOCAL_DB_HOST}:{self.LOCAL_DB_PORT}/{self.LOCAL_DB_NAME}"

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