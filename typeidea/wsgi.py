"""
WSGI config for typeidea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings')
profile = os.environ.get("TYPEIDEA_PROFILE", 'develop')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'typeidea.settings.%s' % profile)
#通过读取系统环境变量中的TYPEIDEA_PROFILE控制django加载不同的settings文件， 达到开发使用develop.py配置，线上使用product.py配置的目的

application = get_wsgi_application()

