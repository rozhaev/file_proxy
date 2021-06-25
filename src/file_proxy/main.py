from src.file_proxy.core.application import Application
from src.file_proxy.core.container import ApplicationContainer
from src.file_proxy.settings import Settings


def init_app():
    settings = Settings()
    application = Application(settings, ApplicationContainer)
    return application


app = init_app()
