from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main-page'),
    path('about', views.about, name='about-page'),
    path('table', views.table, name='table-page'),
    path('button', views.button, name='button-page'),
]
