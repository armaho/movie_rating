from dotenv import load_dotenv
import os

from .not_configured_error import NotConfiguredError


load_dotenv()
        

def get_env(name: str) -> str:
    conf = os.getenv(name)
    if conf is None:
        raise NotConfiguredError(name)        

    return conf

def get_env_int(name: str):
    return int(get_env(name))

