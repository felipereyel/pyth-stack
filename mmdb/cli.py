import fire

from mmdb.config import get_config
from mmdb.server.interface import serve


class CLI(object):
    def serve(self):
        config = get_config()
        serve(config)


def main():
    fire.Fire(CLI)


if __name__ == "__main__":
    main()
