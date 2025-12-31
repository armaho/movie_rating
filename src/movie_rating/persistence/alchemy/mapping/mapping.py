from sqlalchemy import DateTime, ForeignKey, MetaData, Table, Column, String, Integer
from sqlalchemy.orm import registry, relationship

from ...model import Director, Genre, Movie, Rating


metadata = MetaData()
mapper_registry = registry(metadata=metadata)

directors_table = Table(
    "directors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(Director.MAX_NAME_LEN), nullable=False),
    Column("birth_year", Integer, nullable=False),
    Column("description", String(Director.MAX_DESC_LEN), nullable=True),
)
mapper_registry.map_imperatively(
    Director,
    directors_table,
)

movie_genre_table = Table(
    "movie_genre",
    metadata,
    Column(
        "movie_id",
        Integer,
        ForeignKey("movies.id"),
        primary_key=True,
    ),
    Column(
        "genre_id",
        Integer,
        ForeignKey("genres.id"),
        primary_key=True,
    ),
)

genres_table = Table(
    "genres",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(Genre.MAX_NAME_LEN), nullable=False),
    Column("description", String(Genre.MAX_DESC_LEN), nullable=True),
)
mapper_registry.map_imperatively(
    Genre,
    genres_table,
    properties={
        "movies": relationship(
            Movie,
            secondary=movie_genre_table,
            back_populates="genres",
        ),
    },
)

movies_table = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(Movie.MAX_TITLE_LEN), nullable=False),
    Column("release_year", Integer, nullable=False),
    Column(
        "director_id",
        Integer,
        ForeignKey("directors.id"),
        nullable=False,
    ),
)
mapper_registry.map_imperatively(
    Movie,
    movies_table,
    properties={
        "director": relationship(Director),
        "genres": relationship(
            Genre,
            secondary=movie_genre_table,
            back_populates="movies",
        ),
    },
)

ratings_table = Table(
    "ratings",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "movie_id",
        Integer,
        ForeignKey("movies.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("score", Integer, nullable=False),
)
mapper_registry.map_imperatively(
    Rating,
    ratings_table,
    properties={
        "movie": relationship(Movie),
    },
)

