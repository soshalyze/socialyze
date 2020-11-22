import praw
from django.contrib.auth import authenticate
from app.models import *


class RedditCommunication:
    def __init__(self, request, reddit_username):
        self.app_user = request.user.username
        self.reddit = praw.Reddit(client_id='CLIENT_ID',
                                  client_secret='CLIENT_SECRET',
                                  username='USERNAME',
                                  password='PASSWORD',
                                  user_agent='python:commentreader:v0.1 (by u/socialyze_user)')
        self.reddit_user = self.reddit.redditor(reddit_username)
        self.db_user = RedditUser(app_user=self.app_user, username=reddit_username)
        self.db_user.save()

    def fetch_comments(self):
        for comment in self.reddit_user.comments.new(limit=100):
            db_comment = RedditComment(username=self.db_user,
                                       date=comment.created_utc,
                                       content=comment.body,
                                       score=comment.score,
                                       subreddit=comment.subreddit)
            db_comment.save()

    def fetch_posts(self):
        for post in self.reddit_user.submissions.new(limit=50):
            db_post = RedditPost(username=self.db_user,
                                 date=post.created_utc,
                                 title=post.title,
                                 is_text=post.is_self,
                                 subreddit=post.subreddit,
                                 score=post.score)
            db_post.save()
