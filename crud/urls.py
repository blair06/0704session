"""crud URL Configuration

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
from django.urls import path,include #django의 urls로 부터 include를 가져와라->url을 각 app에서 개별적으로 관리할 수 있게한다.
import viewcrud.urls
import viewcrud.views
#import classcrud.urls
#import classcrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewcrud.views.welcome, name = "welcome"),
    path('funccrud/', include(viewcrud.urls)),
    #path('classcrud/', include(classcrud.urls)),
]
