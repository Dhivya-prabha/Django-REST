Add INSTALLED_APPS:
 'upload',
 'rest_framework'


change DB setting:
 'ENGINE': 'django.db.backends.sqlite3',
 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),


TEMPLATES :
 'DIRS': [os.path.join(BASE_DIR, 'templates')],

