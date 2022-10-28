from django.urls import path, include
from . import views
from . views import BookAPIView, BookDetail, GenericAPIView, BookViewSet
from rest_framework.routers import DefaultRouter    # FOR ROUTING IN VIEWSET


router = DefaultRouter()     #SET DEFAULT-ROUTER TO VARIABLE( DJANGO DOCS)
router.register('book', BookViewSet, basename = 'book')  # REGISTER VIEWS AND QS FOR VIEWSET ROUTING


urlpatterns = [
    #path('book/', views.book),  # FUNCTION BASED VIEW
    #path('book/<int:pk>/', views.book_detail),  # FUNCTION BASED DETAIL VIEW

    #path('book/', views.book_list),   # API VIEW DECORATOR FUNCTION
    #path('book/<int:pk>/', views.book_detail),  # API DETAIL-VIEW DECORATOR FUNCTION

    #path('book/', BookAPIView.as_view()),   # class based api view
    #path('book/<int:id>/', BookDetail.as_view()),  # class based detail view

    path('generic/book/<int:id>/', GenericAPIView.as_view()),  # GENERICS AND MIXIN URL PATH

    #path('bookviewset/',include(router.urls)), # URL FOR ROUTING IN VIEWSET(http://localhost:8000/api/bookviewset/book/1/)
    #path('bookviewset/<int:pk>/', include(router.urls)), #http://localhost:8000/api/bookviewset/book/1/

    path('bookviewset/',include(router.urls)), # URL FOR ROUTING IN GENERIC VIEWSET
    path('bookviewset/<int:pk>/', include(router.urls)), #http://localhost:8000/api/bookviewset/book/1/
]
