#-*- encoding:utf-8 -*-
'''
Created on 2014年7月27日

@author: mokan
'''

import os

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT= os.path.join(PROJECT_PATH,'..','media')