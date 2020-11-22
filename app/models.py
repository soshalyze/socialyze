from django.db import models
from django.contrib.auth.models import User


class RedditUser(models.Model):
    app_user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField()

    def create(self, app_user, username):


class RedditPost(models.Model):
    username = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField()
    is_text = models.BooleanField()
    subreddit = models.CharField()
    score = models.IntegerField()


class RedditComment(models.Model):
    username = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    date = models.DateTimeField()
    content = models.TextField()
    score = models.IntegerField()
    subreddit = models.CharField()
