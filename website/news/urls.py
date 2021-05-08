from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news-page'),
    path('create', views.create, name='create')

]
