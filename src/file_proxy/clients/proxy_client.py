from typing import AsyncGenerator

import aiohttp

from src.file_proxy.settings import Settings


class ProxyClient:

    def __init__(self, settings: Settings) -> None:
        self.service_name = settings.service_name
        self.proxy_gateway_url = settings.proxy_gateway_url
        self.buffer_chunk_size = settings.buffer_chunk_size
        self.file_client_id = settings.file_client_id

    def get_header(self) -> dict:
        return {
            'file_client_id': self.file_client_id
        }

    async def get_async_audio_iterator(self, file_id: str) -> AsyncGenerator[bytes, None]:
        url = f'{self.proxy_gateway_url}/{file_id}/download'

        async with aiohttp.ClientSession(headers=self.get_header()) as session:
            async with session.get(url, timeout=None) as response:
                chunk = await response.content.read(self.buffer_chunk_size)
                while chunk:
                    yield chunk
                    chunk = await response.content.read(self.buffer_chunk_size)
