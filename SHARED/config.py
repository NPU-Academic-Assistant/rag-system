from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int 
    postgres_name: str
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