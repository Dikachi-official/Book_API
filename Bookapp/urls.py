from django.urls import path
from . import views
from . views import BookAPIView, BookDetail

urlpatterns = [
    #path('book/', views.book),  # FUNCTION BASED VIEW
    #path('book/<int:pk>/', views.book_detail),  # FUNCTION BASED DETAIL VIEW

    #path('book/', views.book_list),   # API VIEW DECORATOR FUNCTION
    #path('book/<int:pk>/', views.book_detail),  # API DETAIL-VIEW DECORATOR FUNCTION

    path('book/', BookAPIView.as_view()),   # class based api view
    path('book/<int:id>/', BookDetail.as_view())  # class based detail view

]
