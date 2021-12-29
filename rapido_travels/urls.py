"""rapido_travels URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
import rapido
from rapido import views

admin.autodiscover()


# from django.contrib.auth.models import User
# from rest_framework import serializers, viewsets, routers
# from rapido.views import UserViewSet

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
  # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^rapido/',include('rapido.urls'))
    # ,url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns += patterns('',url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)

if settings.DEBUG is False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = rapido.views.handler404

handler500 = rapido.views.handler500
