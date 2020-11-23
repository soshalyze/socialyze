from django.db import models
from django.contrib.auth.models import User


class RedditUserManager(models.Manager):
    # check if the app user has a corresponding reddit user assigned to him
    def app_user_has_reddit_user(self, app_user, reddit_user):
        return super().get_queryset().filter(app_user=app_user, username=reddit_user).exists()

    # check if reddit user exists at all
    def reddit_user_exists(self, reddit_user):
        return super().get_queryset().filter(username=reddit_user).exists()

    def app_user_dataset_users(self, app_user):
        return super().get_queryset().filter(app_user=app_user)


class RedditPostManager(models.Manager):
    def get_all_posts(self, user):
        return super().get_queryset().filter(username_id=user)

    def has_geq_n_posts(self, user, n):
        return self.get_all_posts(user).count() >= n

    def get_subreddit_posts(self, user, subname):
        return self.get_all_posts(user).filter(subreddit=subname)

    def get_post_karma_by_sub(self, user):
        sub_scores = {}
        for post in self.get_all_posts(user):
            if post.subreddit in sub_scores.keys():
                sub_scores[post.subreddit] += post.score
            else:
                sub_scores[post.subreddit] = 0
                sub_scores[post.subreddit] += post.score
            sub_scores[post.subreddit] += post.score
        return sub_scores


class RedditCommentManager(models.Manager):
    def get_all_comments(self, user):
        return super().get_queryset().filter(username_id=user)

    def has_geq_n_comments(self, user, n):
        return self.get_all_comments(user).count() >= n

    def get_subreddit_comments(self, user, subname):
        return self.get_all_comments(user).filter(subreddit=subname)

    def get_comment_karma_by_sub(self, user):
        sub_scores = {}
        for comment in self.get_all_comments(user):
            if comment.subreddit in sub_scores.keys():
                sub_scores[comment.subreddit] += comment.score
            else:
                sub_scores[comment.subreddit] = 0
                sub_scores[comment.subreddit] += comment.score
        return sub_scores


class RedditUser(models.Model):
    app_user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    objects = RedditUserManager()

    def __str__(self):
        return self.username


class RedditPost(models.Model):
    username = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    date = models.BigIntegerField()
    title = models.CharField(max_length=300)
    is_text = models.BooleanField()
    subreddit = models.CharField(max_length=21)
    score = models.IntegerField()
    objects = RedditPostManager()

    def __str__(self):
        return self.title


class RedditComment(models.Model):
    username = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    date = models.BigIntegerField()
    content = models.TextField()
    score = models.IntegerField()
    subreddit = models.CharField(max_length=21)
    objects = RedditCommentManager()

    def __str__(self):
        return '{} : {}'.format(self.username.username, self.date)
