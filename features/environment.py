from django.contrib.auth.models import User
from app.reddit_comm import RedditCommunication
from django.test.client import Client


def before_all(context):
    testuser = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
    comm = RedditCommunication(testuser, reddit_user='thisisbillgates')
    comm.fetch_comments(limit=10)


def after_scenario(context, scenario):
    context.test.client.logout()

