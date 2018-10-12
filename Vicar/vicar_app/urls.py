from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('game/', views.index, name='index'),
    path('game/<int:pk>/',views.detail, name='game'),
    path('game/add/', views.add, name='add')
]
