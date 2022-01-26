# backend/server/server/settings.py

MEDIA_URL = '/media/'
STATIC_URL = '/django_static/' 
STATIC_ROOT = BASE_DIR / 'django_static'


# MEDIA_URL - it is URL for serving files uploaded to Django application, we will use it in future posts.
# STATIC_ROOT - it is a directory where static files from Django application will be stored after running 
#               collectstatic command. The nginx will point to this path.