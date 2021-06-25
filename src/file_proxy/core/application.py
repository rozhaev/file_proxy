import http
from typing import Type

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.file_proxy.controllers.file_controller import router as file_routing
from src.file_proxy.core.container import ApplicationContainer
from src.file_proxy.core.exception import ExceptionModel
from src.file_proxy.settings import Settings


class Application(FastAPI):

    def __init__(self, settings: Settings, container_clazz: Type[ApplicationContainer]) -> None:
        super().__init__(title=settings.service_title)
        self.container_clazz = container_clazz
        self.__init_cors(settings)
        self.__init_routes()

    def __init_cors(self, settings: Settings) -> None:
        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __init_routes(self) -> None:
        file_routing.responses[http.HTTPStatus.NOT_FOUND] = ExceptionModel
        self.include_router(file_routing)
