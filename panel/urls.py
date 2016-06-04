from django.conf.urls import url
from django.contrib import admin


from .views import (
    panel_list,
    panel_create,
    panel_detail,
    panel_update,
    panel_delete,
    )


urlpatterns = [
	url(r'^$', panel_list, name="list"),
    url(r'^create/$', panel_create),
    url(r'^(?P<id>\d+)/$', panel_detail, name="detail"), #Use id to identify different Cell Type Panel
    url(r'^(?P<id>\d+)/edit/$', panel_update, name="update"),
    url(r'^(?P<id>\d+)/delete/$', panel_delete),
    # $ means once address is more than panel/, it will not directed to this view
    # url(r'^panel/$', '<appname>.views.<function_name>'),
]