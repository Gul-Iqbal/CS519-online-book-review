########### Import necessary Django modules ###########
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from books.models import Review, Wishlist
from .models import Profile


########### Define the home view, rendering the home page ###########
def home(request):
    return render(request, 'accounts/home.html')


########### Define the register view to handle user registration ###########
def register(request):
    ########### Check if the request method is POST (form submitted) ###########
    if request.method == 'POST':
        ########### Retrieve form data from the request ###########
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        ########### Check if the two entered passwords match ###########
        if password1 != password2:
            messages.error(request, "Passwords do not match!")  # Display error message
            return redirect('register')  # Redirect back to registration page

        ########### Check if the username already exists in the database ###########
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")  # Display error message
            return redirect('register')  # Redirect back to registration page

        ########### Check if the email is already registered ###########
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")  # Display error message
            return redirect('register')  # Redirect back to registration page

        ########### Create the new user since validations passed ###########
        user = User.objects.create_user(username=username, email=email, password=password1)

        ########### Automatically log the user in after registration ###########
        login(request, user)

        ########### Show a success message and redirect to profile page ###########
        messages.success(request, "Account created successfully!")
        return redirect('profile')

    ########### If GET request, simply render the registration form ###########
    return render(request, 'accounts/register.html')


########### Define the profile view that is only accessible to logged-in users ###########
@login_required
def profile(request):
    ########### Render the profile page for the logged-in user ###########
    return render(request, 'accounts/profile.html')


########### Define the login view to handle user login ###########
def login_view(request):
    ########### Check if the request method is POST (form submitted) ###########
    if request.method == 'POST':
        ########### Retrieve username and password from the submitted form ###########
        username = request.POST['username']
        password = request.POST['password']

        ########### Authenticate the user credentials ###########
        user = authenticate(request, username=username, password=password)

        ########### If authentication is successful ###########
        if user is not None:
            auth_login(request, user)  # Log the user in
            return redirect('profile')  # Redirect to the profile page
        else:
            ########### If authentication fails, show error message ###########
            messages.error(request, "Invalid username or password.")
            return redirect('login')  # Redirect back to login page

    ########### If GET request, render the login form ###########
    return render(request, 'accounts/login.html')


########### Define the logout view to handle user logout ###########
def logout_view(request):
    auth_logout(request)  ########### Log the user out and end their session ###########
    messages.success(request, "You have been logged out.")  ########### Show a success message ###########
    return redirect('login')  ########### Redirect the user to the login page ###########


############ Define the profile view to display user reviews ###########
@login_required
def profile(request):
    user_reviews = Review.objects.filter(user=request.user)
    wishlist_books = Wishlist.objects.filter(user=request.user)

    return render(request, 'accounts/profile.html', {
        'user_reviews': user_reviews,
        'wishlist_books': wishlist_books,
    })


############ Define the about and contact views ###########
def about(request):
    return render(request, 'accounts/about.html')


############ Define the contact view ###########
def contact(request):
    return render(request, 'accounts/contact.html')


@login_required
def profile(request):
    user_reviews = Review.objects.filter(user=request.user)
    wishlist_books = Wishlist.objects.filter(user=request.user)

    # This line will create a Profile if it doesn't exist
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, 'accounts/profile.html', {
        'user_reviews': user_reviews,
        'wishlist_books': wishlist_books,
        'profile': profile,
    })
