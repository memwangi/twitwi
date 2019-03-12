from django.shortcuts import render
from .models import Twit
from django.contrib.auth.decorators import login_required


def feed(request):
    userids = []

    for user in request.user.twitwiprofile.follows.all():
        userids.append(user.id)

    userids.append(request.user.id)
    twits = Twit.objects.filter(user_id__in=userids)

    return render(request, 'twit/feed.html', {'twits': twits})
