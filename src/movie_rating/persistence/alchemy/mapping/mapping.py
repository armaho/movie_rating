from sqlalchemy import DateTime, ForeignKey, MetaData, Table, Column, String, Integer
from sqlalchemy.orm import registry, relationship

metadata = MetaData()

mapper_registry = registry()

