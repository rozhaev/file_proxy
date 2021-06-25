from pathlib import Path

from pydantic import BaseSettings

base_dir = Path(__file__).parent.parent.parent.absolute()


class Settings(BaseSettings):
    service_name: str
    service_title: str = "Proxy test service"
    proxy_gateway_url: str
    buffer_chunk_size: int
    file_client_id: str = 'proxy_test_service_001'

    class Config:
        env_file = f'{base_dir}/.env'
