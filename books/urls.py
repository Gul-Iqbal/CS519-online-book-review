from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # List of all books
    path('<int:book_id>/', views.book_detail, name='book_detail'),  # Details of a specific book
    path('<int:book_id>/wishlist/', views.add_to_wishlist, name='add_to_wishlist'), # Add book to wishlist
    path('review/<int:review_id>/report/', views.report_review, name='report_review'), # Report a review
    path('add/', views.add_book, name='add_book'), # Add a new book
]