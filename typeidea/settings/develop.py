from .base import *    #NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
#开发环境把数据库和DEBUG配置剪切过来，生产环境；不能要DEBUG
#之后修改manage.py和wsgi.py中settings的路径
