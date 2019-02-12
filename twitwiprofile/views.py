from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from twitwiprofile.forms import SignInForm, SignUpForm


def frontpage(request):
    if request.user.is_authenticated:
        # Redirect to user's profile
        return render(request, 'twitwiprofile/profile.html')
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
    user = User.objects.get(username=username)

    return render(request, 'twitwiprofile/profile.html', {'user': user})
