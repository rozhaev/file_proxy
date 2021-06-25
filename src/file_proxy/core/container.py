from typing import Iterator

from injector import Module, singleton, provider, Injector
from starlette.requests import Request

from src.file_proxy.clients.proxy_client import ProxyClient
from src.file_proxy.settings import Settings


class ApplicationContainer(Module):

    @singleton
    @provider
    def provide_settings(self) -> Settings:
        return Settings()

    @singleton
    @provider
    def provide_crypto_gateway_client(self, settings: Settings) -> ProxyClient:
        return ProxyClient(settings)


async def get_container_injector(request: Request) -> Iterator[Injector]:
    container = Injector(request.app.container_clazz())
    try:
        yield container
    finally:
        del container
