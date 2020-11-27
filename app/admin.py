from django.contrib import admin
from app.models import RedditUser, RedditPost, RedditComment

admin.site.register(RedditUser)
admin.site.register(RedditPost)
admin.site.register(RedditComment)

