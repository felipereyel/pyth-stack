import uvicorn

from mmdb.config import Config
from mmdb.server.app import get_app


def serve(config: Config):
    app = get_app(config)

    uvicorn.run(
        app,
        host=config.host,
        port=config.port,
        log_level=config.log_level,
    )
