from django.urls import path
from . import views

# Mamy tutaj sciezke / adres url
# http://127.0.0.1:8000/members/

urlpatterns = [
    path('', views.main, name='main'),
    path('categories/', views.categories, name='categories'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]