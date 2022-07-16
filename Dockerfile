# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.9-slim-buster

# Add user that will be used in the container.
RUN useradd wagtail

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

# Install the application server.
RUN pip install "gunicorn==20.0.4"

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Install the project requirements.
COPY ./portfolio/requirements.txt /app
RUN pip install -r requirements.txt


# Set this directory to be owned by the "wagtail" user. This Wagtail project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail ./portfolio /app

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# Collect static files.
RUN python manage.py collectstatic --noinput --clear

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=portfolio.settings.prod

# Port used by this container to serve HTTP.
ARG PORT
ENV PORT=$PORT
EXPOSE $PORT

RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint.sh"]
