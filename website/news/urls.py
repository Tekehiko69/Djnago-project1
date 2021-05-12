from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news-page'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='details-page'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update-page'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete-page'),
]
