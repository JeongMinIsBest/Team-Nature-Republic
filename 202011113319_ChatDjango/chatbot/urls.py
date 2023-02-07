from django.urls import path
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('chattrain', views.chattrain, name="chattrain"),
    path('chatanswer', views.chatanswer, name="chatanswer"),
]
