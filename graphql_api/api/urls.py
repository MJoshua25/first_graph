from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path("", index, name="index"),
    path('category/<str:pk>',category,name='category'),
    path('ingredient/',ingredient,name='ingredient'),
]