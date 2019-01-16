from django.urls import path
from . import views

app_name = 'task2app'

urlpatterns = [
    path('', views.index, name='index'),
    path('task2app/', views.home, name='home')
]