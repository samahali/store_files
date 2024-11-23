FROM python:3.13-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Copy the project code into the container
COPY . /app/

# Install PostgreSQL client tools
RUN apk add --no-cache postgresql-client postgresql-dev build-base


# Copy requirements and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


