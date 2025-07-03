########### Import necessary Django modules ###########
from django.db import models
from django.contrib.auth.models import User

########### Define the Book model to store book information ###########
class Book(models.Model):
    title = models.CharField(max_length=200)  ########### Title of the book ###########
    author = models.CharField(max_length=100)  ########### Author name ###########
    genre = models.CharField(max_length=50)  ########### Genre or category of the book ###########
    description = models.TextField()  ########### Detailed description about the book ###########
    year = models.IntegerField()  ########### Year of publication ###########
    cover_image = models.ImageField(upload_to='book_covers/', blank=True)  ########### Optional cover image ###########

    ########### String representation of a book (shows the title) ###########
    def __str__(self):
        return self.title

########### Define the Review model to store user reviews for books ###########
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_reported = models.BooleanField(default=False)  # NEW field to track if review is flagged

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

############ Define the Wishlist model to store user's wishlist items ###########
class Wishlist(models.Model): ############ Link wishlist item to a specific user ###########
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_items') ############ Link wishlist item to a specific book ###########
    book = models.ForeignKey(Book, on_delete=models.CASCADE) ############ Automatically set the date when the wishlist item was added ###########
    added_at = models.DateTimeField(auto_now_add=True) ############ String representation of a wishlist item (shows username and book title) ###########

    def __str__(self): ############ String representation of a wishlist item (shows username and book title) ###########
        return f"{self.user.username} - {self.book.title}" ############ Meta class to define additional options for the Wishlist model ###########
