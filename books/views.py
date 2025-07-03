from django.shortcuts import get_object_or_404, redirect, render  # Import necessary functions
from .models import Book, Review  # Import models
from django.contrib.auth.decorators import login_required  # Import decorator for login required
from django.db import models  # Needed for aggregation (Avg)
from .models import Wishlist # Import Wishlist model
from django.contrib.admin.views.decorators import staff_member_required
from .forms import BookForm
from django.contrib import messages



def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id) # Get the book object or return 404 if not found
    reviews = book.reviews.all() # Get all reviews related to the book
    average_rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] # Calculate average rating of the book

    # Simple Recommendation: Suggest 3 random books with the same genre (excluding the current book)
    recommended_books = Book.objects.filter(genre=book.genre).exclude(id=book.id).order_by('?')[:3] # Get 3 random books of the same genre

    if request.method == 'POST': # Handle form submission
        if request.user.is_authenticated: # Check if user is authenticated
            rating = request.POST.get('rating') # Get rating from the form
            comment = request.POST.get('comment') # Get comment from the form

            Review.objects.create( # Create a new review
                book=book, # Associate review with the book
                user=request.user, # Associate review with the user
                rating=rating, # Set rating
                comment=comment # Set comment
            )
            return redirect('book_detail', book_id=book.id) # Redirect to the book detail page after submission
        else: # If user is not authenticated, redirect to login page
            return redirect('login') # Redirect to login page

    return render(request, 'books/book_detail.html', { # Render the book detail page
        'book': book, # Pass the book object
        'reviews': reviews, # Pass the reviews
        'average_rating': average_rating, # Pass the average
        'recommended_books': recommended_books # Pass the recommended books
    })



def book_list(request): # Function to list all books
    books = Book.objects.all() # Get all books from the database
    return render(request, 'books/book_list.html', {'books': books}) # Render the book list page with all books



# Function to handle adding a book to the wishlist
@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Check if already exists
    existing = Wishlist.objects.filter(user=request.user, book=book)
    if not existing:
        Wishlist.objects.create(user=request.user, book=book)

    return redirect('book_detail', book_id=book_id)


# Function to handle removing a book from the wishlist
@login_required
def report_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.is_reported = True
    review.save()
    messages.success(request, "Review reported successfully!")
    return redirect('book_detail', book_id=review.book.id)



# Function to handle adding a book
@staff_member_required  # Only staff/admin can access
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


