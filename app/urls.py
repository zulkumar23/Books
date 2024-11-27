from django.urls import path
from .  import  views

urlpatterns = [
    path('books_list/', views.book_list_view),
    path('books_create/', views.book_create_view),
    path('books_list/<int:pk>/', views.book_detail_view),
    path('books_update/<int:pk>/', views.book_update_view)
]
