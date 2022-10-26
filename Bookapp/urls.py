from django.urls import path, include
from . import views

urlpatterns = [
    #path('book/', views.book),
    #path('book/<int:pk>/', views.book_detail),
    path('book/', views.book_list),
    path('book/<int:pk>/', views.book_detail),
]
