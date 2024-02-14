from django.urls import path
from drinks import views

urlpatterns = [
    path('', views.index, name='index')
]