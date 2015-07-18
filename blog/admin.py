#-*- encoding:utf-8 -*-
'''
Created on 2014年7月20日

@author: mokan
'''
from django.contrib import admin
from blog.models import *
#admin.site.register(BlogPost,BlogPostAdmin)
#向Admin中注册一个管理模块
admin.site.register(Users)
admin.site.register(EssayType)
admin.site.register(Essay)
admin.site.register(Comment)
admin.site.register(LevelMsg)
admin.site.register(Archive)