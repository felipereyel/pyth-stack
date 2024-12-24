from fasthtml.fastapp import fast_app

from mmdb.config import Config
from mmdb.server.design.pages import Home


def get_app(config: Config):
    app, _ = fast_app()

    @app.get("/")
    def home():
        return Home()

    return app
