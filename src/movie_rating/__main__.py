import sys

from .config import NotConfiguredError, get_env
from .webapi import setup_server


def main():
    port : int
    try:
        port = int(get_env("SERVER_PORT"))
    except NotConfiguredError as nce:
        print("error: {nce}")
        sys.exit(1)
    except ValueError as ve:
        print("error: invalid SERVER_PORT")
        sys.exit(1)

    setup_server(port)


if __name__ == "__main__":
    main()

