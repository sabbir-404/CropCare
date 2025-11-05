"""
Django settings for practice1 project (dev).
"""

from pathlib import Path

# ---------------------------------------
# PATHS
# ---------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------
# CORE FLAGS (DEV)
# ---------------------------------------
DEBUG = True
SECRET_KEY = "django-insecure-da@nrhgs8s)xxr^cub=n40t*=6-7$o&82&8oc1mfh_a)cm!!=j"  # dev only
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# ---------------------------------------
# APPS
# ---------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third-party
    "corsheaders",
    "rest_framework",

    # local
    "api",
]

# ---------------------------------------
# MIDDLEWARE
# ---------------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # keep high (before CommonMiddleware)
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "practice1.urls"

# ---------------------------------------
# TEMPLATES
# ---------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "practice1.wsgi.application"

# ---------------------------------------
# DATABASE (SQLite for dev)
# ---------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ---------------------------------------
# AUTH / PASSWORD VALIDATORS
# ---------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------------------
# I18N / TZ
# ---------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Dhaka"   # <- use local time
USE_I18N = True
USE_TZ = True

# ---------------------------------------
# STATIC / MEDIA
# ---------------------------------------
STATIC_URL = "static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------------------
# REST FRAMEWORK (minimal JSON)
# ---------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

# ---------------------------------------
# CORS / CSRF (Vite dev @5173)
# ---------------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
CORS_ALLOW_CREDENTIALS = False  # set True only if you use cookie-based auth
