from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    chroma_path: str = "./chroma_storage"
    postgresql_user: str
    postgresql_password: str
    postgresql_host: str = "localhost"
    postgresql_port: int = 5432
    postgresql_name: str
    openrouter_api_key: str
    base_url: str 
    teacher_model: str 
    memory_model: str 
    router_model: str

    


settings = Settings()