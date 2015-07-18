#-*- encoding:utf-8 -*-
from django.conf.urls import patterns, url
urlpatterns = patterns('',
    #url(r'^$',archive),
    #url(r'root/(?P<path>.*)$', 'django.views.static.serve',{'document_root': 'D:/Aptana Studio Workspace/blog/views/temp'}), 
    url(r'^essay/(?P<eid>\d+)/$','blog.views.essay_details'),
    url(r'^search/$','blog.views.search'),
    url(r'^leavemsg/(?P<eid>\d+)/$','blog.views.leave_comment'),
    url(r'^(?P<etype>\d+)/(?P<pageNo>\d+)/$','blog.views.index'),
    url(r'^aboutme','blog.views.aboutme'),
    url(r'^chatroom$','blog.views.chatroom'),
    url(r'^chat$','blog.views.chat'),
    url(r'^','blog.views.index')
)