import praw
from app.models import RedditUser

class RedditCommunication:
    def __init__(self, reddit_user):
        self.reddit = praw.Reddit(client_id='CLIENT_ID',
                                  client_secret='CLIENT_SECRET',
                                  username='USERNAME',
                                  password='PASSWORD',
                                  user_agent='socialyze')
        self.reddit_user = self.reddit.redditor(reddit_user)

    def fetch_comments(self):
        for comment in self.reddit_user.comments.new(limit=100):


