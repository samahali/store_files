#!/bin/sh

echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h db -p 5432; do
  sleep 1
done
echo "PostgreSQL is ready"
# Run database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start the Django development server
python manage.py runserver 0.0.0.0:8000