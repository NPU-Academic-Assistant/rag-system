from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    postgresql_user: str
    postgresql_password: str
    postgresql_host: str
    postgresql_port: int 
    postgresql_name: str
    chromadb_user: str
    chromadb_password: str 
    chromadb_host: str
    chromadb_port: int
    chromadb_name: str 
    openrouter_api_key: str
    base_url: str 
    teacher_model: str 
    memory_model: str 
    router_model: str

    


settings = Settings()