"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1.views import RegisterAPI
from app1.views import LoginView
from knox import views as knox_views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.static import serve
# from django.conf.urls import re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginView.as_view()),
    # path(r' ^media/(?p<path>.*)$' ,serve,{'document_root':    settings.MEDIA_ROOT}),
    # path(r' ^static/(?p<path>.*)$',serve,{'document_root':settings.STATIC_ROOT})
    
]
# urlpatterns =urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)