from fasthtml.components import Div, P
from fasthtml.fastapp import fast_app

from mmdb.config import Config

# from fasthtml.xtend import Titled


def get_app(config: Config):
    app, rt = fast_app()

    @rt("/")
    def get():
        return Div(P("Hello World!"), hx_get="/change")

    return app
