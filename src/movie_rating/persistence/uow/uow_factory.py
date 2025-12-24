import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ...config import get_env, NotConfiguredError

_session_factory = None


def get_session_factory() -> sessionmaker:
    global _session_factory
    if _session_factory is None:
        db_url: str
        try:
            db_url = get_env("DB_URL")
        except NotConfiguredError as nce:
            print(f"error: {nce}")
            sys.exit(1)

        engine = create_engine(db_url, echo=True)
        _session_factory = sessionmaker(bind=engine)

    return _session_factory


def get_uow():
    from ..alchemy.uow import AlchemyUnitOfWork

    return AlchemyUnitOfWork(get_session_factory())
