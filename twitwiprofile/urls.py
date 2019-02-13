
from django.urls import path

from .views import frontpage, signout, profile
from twit.views import feed

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('feed/', feed, name='signout'),
    path('signout/', signout, name='signout'),
    path('<str:username>/', profile, name='profile')
]
