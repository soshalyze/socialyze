from django.db import models
from django.contrib.auth.models import User


class RedditPostManager(models.Manager):
    def get_all_posts(self, user):
        return super().get_queryset().filter(app_user=user)

    def get_subreddit_posts(self, user, subname):
        return self.get_all_posts(user).filter(subreddit=subname)


class RedditCommentManager(models.Manager):
    def get_all_comments(self, user):
        return super().get_queryset().filter(app_user=user)

    def get_subreddit_comments(self, user, subname):
        return self.get_all_comments(user).filter(subreddit=subname)


class RedditUser(models.Model):
    app_user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField()


class RedditPost(models.Model):
    username = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    date = models.BigIntegerField()
    title = models.CharField()
    is_text = models.BooleanField()
    subreddit = models.CharField()
    score = models.IntegerField()


class RedditComment(models.Model):
    username = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    date = models.BigIntegerField()
    content = models.TextField()
    score = models.IntegerField()
    subreddit = models.CharField()
