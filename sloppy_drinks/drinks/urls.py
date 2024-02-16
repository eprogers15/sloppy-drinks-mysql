from django.urls import path
from drinks import views

urlpatterns = [
    path('', views.drink_index, name='drink_index'),
    path("<slug:slug>/", views.drink_detail, name="drink_detail"),
]