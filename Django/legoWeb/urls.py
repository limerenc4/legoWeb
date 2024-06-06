from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_question, name='add'),
    path('add-page/', views.add_page, name='add-page'),
    path('questions/', views.show_all_question, name='questions'),
]
