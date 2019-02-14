
from django.urls import path

from .views import frontpage, signout, profile, followers, follows, unfollow, follow
from twit.views import feed

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('feed/', feed, name='feed'),
    path('signout/', signout, name='signout'),
    path('<str:username>/follows/', follows, name='follows'),
    path('<str:username>/followers/', followers, name='followers'),
    path('<str:username>/follow/', follow, name='follow'),
    path('<str:username>/unfollow/', unfollow, name='unfollow'),
    path('<str:username>/', profile, name='profile')
]
