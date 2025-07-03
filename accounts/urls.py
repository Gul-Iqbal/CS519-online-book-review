########### Import necessary Django modules ###########
from django.urls import path
from . import views

########### Define URL patterns and link them to corresponding view functions ###########
urlpatterns = [
    ########### URL pattern for the home page ###########
    path('', views.home, name='home'),

    ########### URL pattern for the registration page ###########
    path('register/', views.register, name='register'),

    ########### URL pattern for the profile page (only accessible after login) ###########
    path('profile/', views.profile, name='profile'),

    ########### URL pattern for the login page ###########
    path('login/', views.login_view, name='login'),

    ########### URL pattern for the logout action ###########
    path('logout/', views.logout_view, name='logout'),
    ########### URL pattern for password reset ###########
    path('about/', views.about, name='about'),
    ########### URL pattern for the contact page ###########
    path('contact/', views.contact, name='contact'),
]
