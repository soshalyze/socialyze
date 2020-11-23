import praw
from app.models import *


class RedditCommunication:
    def __init__(self, app_user, reddit_user):
        self.app_user = app_user
        self.reddit = praw.Reddit(client_id='CLIENT_ID',
                                  client_secret='CLIENT_SECRET',
                                  username='USERNAME',
                                  password='PASSWORD',
                                  user_agent='python:commentreader:v0.1')
        self.redditor = self.reddit.redditor(reddit_user)
        self.db_user = RedditUser(app_user=self.app_user, username=reddit_user)
        self.db_user.save()

    def fetch_comments(self, limit):
        for comment in self.redditor.comments.new(limit=limit):
            db_comment = RedditComment(username=self.db_user,
                                       date=comment.created_utc,
                                       content=comment.body,
                                       score=comment.score,
                                       subreddit=comment.subreddit)
            db_comment.save()

    def fetch_posts(self, limit):
        for post in self.redditor.submissions.new(limit=limit):
            db_post = RedditPost(username=self.db_user,
                                 date=post.created_utc,
                                 title=post.title,
                                 is_text=post.is_self,
                                 subreddit=post.subreddit,
                                 score=post.score)
            db_post.save()
