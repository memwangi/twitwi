from django.db import models
from django.contrib.auth.models import User


class TwitwiProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    follows = models.ManyToManyField(
        "self", related_name='followed_by', symmetrical=False)


"""
 Automatically create a profile when a user is created so that
 we don't have to think about creating it ourself
"""
User.TwitwiProfile = property(
    lambda u: TwitwiProfile.objects.get_or_create(user=u)[0])
