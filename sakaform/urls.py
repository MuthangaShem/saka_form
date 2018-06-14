"""sakaform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    # url(r'^$', views.HomePage.as_view(), name='home'),

    url(r'', include('app.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
# >>>>>>> 5621387e0888a58f5dc24579ce31704187eb6729
=======
    url(r'^$', views.home, name='home'),
    url(r'^event/', include('app.urls', namespace='event')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de
]
