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
from django.contrib import admin
from pdsoauth.views import index
from pdsapi.views import contact_returns, accept_command, get_user_contact

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('registration.backends.default.urls', namespace='registration')),
    url(r'^$', index),
    url(r'^contact_returns/$', contact_returns, name='contact'),
    url(r'^api/v1/commands/$', accept_command, name='accept_command'),
    url(r'^api/v1/user/contact/$', get_user_contact, name='get_user_contact'),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
