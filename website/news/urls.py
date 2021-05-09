from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news-page'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewDetailView.as_view(), name='details-page')

]
