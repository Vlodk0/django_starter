from django.urls import path
from lesson_5 import views

urlpatterns = [
    path('try-form/', views.my_form, name='my_form'),
]