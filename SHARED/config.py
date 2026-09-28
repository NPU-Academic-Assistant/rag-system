from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    chroma_path: str = "./chroma_storage"
    embedding_model: str = "/home/rahim/.cache/modelscope/models/BAAI--bge-small-en-v1.5/snapshots/master"
    postgresql_user: str
    postgresql_password: str
    postgresql_host: str = "localhost"
    postgresql_port: int = 5432
    postgresql_name: str
    base_url: str = SettingsConfigDict(env_file=".env")
    teacher_model: str = SettingsConfigDict(env_file=".env")
    memory_model: str = SettingsConfigDict(env_file=".env")
    router_model: str = SettingsConfigDict(env_file=".env")

    


settings = Settings()

