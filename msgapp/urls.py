
from django.urls import path
from . import views

# 局部路由
urlpatterns = [
    path("", views.msgproc),
]