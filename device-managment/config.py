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

  @property
  def DATABASE_URL(self):
    if self.MODE == "PROD":
      print(f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
      return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    if self.MODE == "LOCAL":
      print(f"postgresql+asyncpg://{self.LOCAL_DB_USER}:{self.LOCAL_DB_PASS}@{self.LOCAL_DB_HOST}:{self.LOCAL_DB_PORT}/{self.LOCAL_DB_NAME}")
      return f"postgresql+asyncpg://{self.LOCAL_DB_USER}:{self.LOCAL_DB_PASS}@{self.LOCAL_DB_HOST}:{self.LOCAL_DB_PORT}/{self.LOCAL_DB_NAME}"

  model_config = SettingsConfigDict(env_file=".env")

settings = Settings()