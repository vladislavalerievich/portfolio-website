from .base import *
import dj_database_url
import mimetypes

mimetypes.add_type("text/javascript", ".js", True)

DEBUG = False

INSTALLED_APPS += [
    'whitenoise.runserver_nostatic',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': os.environ.get("CLOUDINARY_API_KEY"),
    'API_SECRET': os.environ.get("CLOUDINARY_API_SECRET")
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1', os.environ.get("HOST_NAME")]
ALLOWED_HOSTS = ['localhost','109.106.244.81','www.galaktoza.de', 'galaktoza.de']

# SQLite3 for now, CHANGE THIS LATER
# DATABASE_URL = os.path.join(BASE_DIR, "db.sqlite3") # os.environ.get("DATABASE_URL")
# DATABASES["default"] = dj_database_url.config(default='sqlite:///db.sqlite3') # , conn_max_age=500, ssl_require=True)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
