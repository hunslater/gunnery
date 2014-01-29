from django.conf.urls import patterns, url, include
from .views.main import *
from .views.modal import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^application/(?P<application_id>[\d]+)/$', application_page, name='application_page'),
    url(r'^environment/(?P<environment_id>[\d]+)/$', environment_page, name='environment_page'),
    url(r'^modal/server_test/(?P<server_id>[\d]+)/$', server_test, name='server_test'),
    url(r'^modal/server_test_ajax/(?P<task_id>[\da-z\-]+)/$', server_test_ajax, name='server_test_ajax'),

    url(r'^modal_form/(?P<form_name>[a-z_]+)/$', modal_form, name='modal_form'),
    url(r'^modal_form/(?P<form_name>[a-z_]+)/(?P<id>\d+)/$', modal_form, name='modal_form'),
    url(r'^modal_form/(?P<parent_name>[a-z_]+)/(?P<parent_id>\d+)/(?P<form_name>[a-z_]+)/(?P<id>\d+)?/?$', modal_form, name='modal_form'),
    url(r'^modal_delete/(?P<form_name>[a-z_]+)/(?P<id>\d+)/$', modal_delete, name='modal_delete'),

    url(r'^settings/', settings_page, name='settings_page'),
)