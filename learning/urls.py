"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from app.views import HomePageView, HowToView, TestView, TestRightView, TestWrongView, TestRandomView, generate_simple_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('howto', HowToView.as_view(), name='howto'),
    path('test/<int:difficulty>', TestView.as_view(), name='test'),
    path('test/<int:difficulty>/right', TestRightView.as_view(), name='right'),
    path('test/<int:difficulty>/wrong', TestWrongView.as_view(), name='wrong'),
    path('test/random', TestRandomView.as_view(), name='random'),
    path('generate-simple', generate_simple_view, name='generate_simple'),
]
