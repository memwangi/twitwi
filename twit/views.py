from django.shortcuts import render
from .models import Twit


def feed(request):
    userids = []
    for id in request.user.twitwiprofile.follows.all():
        userids.append(id)

    userids.append(request.user.id)  # To include your own tweets
    twits = Twit.objects.filter(user_id__in=userids)[0:25]

    return render(request, 'twit/feed.html', {'twits': twits})
