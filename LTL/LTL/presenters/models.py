from django.db import models

from LTL.core.models import TimeStampedModel



class Profile(TimeStampedModel):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=255)
    twitter = models.URLField(blank=True, null=True)
    linked_in = models.URLField(blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)
    company = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Talk(TimeStampedModel):
    presenter = models.ForeignKey(Profile)
    title = models.CharField(max_length=255)
    description = models.TextField()
    when = models.DateTimeField()
    topics = models.CharField(max_length=255, null=True, blank=True)

