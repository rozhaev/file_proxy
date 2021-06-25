from typing import Optional

from fastapi import APIRouter
from fastapi_utils.cbv import cbv
from starlette.responses import StreamingResponse

from src.file_proxy.clients.proxy_client import ProxyClient
from src.file_proxy.core.controller import BaseController

router = APIRouter()


@cbv(router)
class FileController(BaseController):

    def __init__(self) -> None:
        super(FileController, self).__init__()
        self.crypto_gateway_client = self.injector.get(ProxyClient)

    @router.get('/download')
    async def download_file(self, file_id: Optional[str]) -> StreamingResponse:
        """Return a async file audio stream."""

        file_iterator = self.crypto_gateway_client.get_async_audio_iterator(file_id)
        return StreamingResponse(file_iterator, media_type="audio/mpeg")
