"""pdsservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
# from django.contrib import admin

from SqlUsers.views import new_sql_user, grant_graph_permission
from pdsapi.views import status_check, get_user_email

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', status_check),
    url(r'^api/v1/user/new/$', new_sql_user, name='new_sql_user'),
    url(r'^api/v1/user/graph/grant/$', grant_graph_permission, name='grant_graph_permission'),
    url(r'^status/$', status_check, name='status_check'),
    url(r'^api/v1/users/(\d+)/emails/$', get_user_email, name='get_user_email'),
]
