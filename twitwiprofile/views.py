from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from twitwiprofile.forms import SignInForm, SignUpForm
from twit.forms import TwitForm


def frontpage(request):
    if request.user.is_authenticated:
        # Redirect to user's profile
        return redirect('/' + request.user.username + '/')
    else:
        if request.method == 'POST':

            # If user is signing up
            if 'signupform' in request.POST:
                signupform = SignUpForm(data=request.POST)
                signinform = SignInForm()

                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')

            # If user is signing in
            else:
                signinform = SignInForm(data=request.POST)
                signupform = SignUpForm()

                if signinform.is_valid():
                    login(request, signinform.get_user())
                    return redirect('/')

        else:
            signupform = SignUpForm()
            signinform = SignInForm()

    return render(request, 'twitwiprofile/frontpage.html', {'signupform': signupform, 'signinform': signinform})


def signout(request):
    """ Log out the current user"""
    logout(request)
    return redirect('/')


def profile(request, username):
    """ Fetch user details using their username, then render their profile on profile.html """
    if request.user.is_authenticated:
        user = User.objects.get(username=username)

        if request.method == 'POST':
            form = TwitForm(data=request.POST)

            if form.is_valid():
                twit = form.save(commit=False)
                twit.user = request.user
                twit.save()

                redirecturl = request.POST.get('redirect', '/')

                return redirect(redirecturl)
        else:
            form = TwitForm()

        return render(request, 'twitwiprofile/profile.html', {'form': form, 'user': user})
    else:
        return redirect('/')


def follows(request, username):
    """
    Get the list of people followed by the current user
    """
    user = User.objects.get(username=username)
    twitwiprofiles = user.twitwiprofile.follows.select_related('user').all()

    return render(request, 'twitwiprofile/users.html', {'title': 'Follows', 'twitwiprofiles': twitwiprofiles})


def followers(request, username):
    """Get a list of people who follow the current user
    """
    user = User.objects.get(username=username)
    twitwiprofiles = user.twitwiprofile.followed_by.select_related('user').all()

    return render(request, 'twitwiprofile/users.html', {'title': 'Followers', 'twitwiprofiles': twitwiprofiles})


@login_required
def unfollow(request, username):
    """Unfollow a user but still redirect to his profile"""
    user = User.objects.get(username=username)
    request.user.twitwiprofile.follows.remove(user.twitwiprofile)

    return redirect('/' + user.username + '/')


@login_required
def follow(request, username):
    """Follow a user and still stay on his profile"""
    user = User.objects.get(username=username)
    request.user.twitwiprofile.follows.add(user.twitwiprofile)

    return redirect('/' + user.username + '/')
