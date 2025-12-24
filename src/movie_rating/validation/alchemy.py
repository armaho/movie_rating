from sqlalchemy import event


def create_listener(callback):
    return lambda mapper, connection, target: callback(target)

def setup_validation_alchemy():
    pass
