"""achievements URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url

from . import views, testdb

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.hello),
    url('xysdys/', views.xysdys),
    url('testdb/', testdb.testdb),

    path('captcha/', include('captcha.urls')),  # 图片验证码 路由
    path('refresh_captcha/', views.refresh_captcha),  # 刷新验证码，ajax
    path('test/', views.IndexView.as_view()),

]
