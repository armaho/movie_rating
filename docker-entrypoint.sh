#!/bin/sh
set -e

if [ -z "$DB_URL" ]; then
  echo "Error: DB_URL is not set"
  exit 1
fi

poetry run alembic upgrade head
poetry run python -m movie_rating
