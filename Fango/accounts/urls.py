# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

app_name = "accounts"
urlpatterns = [
    # URL pattern for the IndexViews
    url(
        regex=r'^$',
        view=views.index,
        name='index'
    ),
    url(
        regex=r'^(?P<account_id>[0-9]+)/$',
        view=views.detail,
        name='detail',
    )

]
