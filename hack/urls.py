"""hack URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from home import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^login/$', auth_views.login),
    url(r'^getinfo/orderid/$',views.getOrdeIdInfo),
    url(r'^ordercheck/(?P<orderid>)',views.ordercheck),
    url(r'^complained/$',views.complained),
    url(r'^imeifulfillment/$',views.imeifulfillment),
    url(r'^getinfo/imei/$',views.getimei),
    url(r'^wrongproduct/$',views.wrongproduct),
    url(r'^logout/$',view=logout,kwargs={'next_page': '/'},name='adminlogout'),

]
