from django import forms
from app.models import RedditUser

SOCIAL_MEDIA_SITES = [
    ('reddit', 'Reddit'),
]

CONTENT_TYPES = [
    ('post', 'Posts'),
    ('comment', 'Comments'),
]

VIS_TYPES = [
    ('karma_by_sub', 'Comment Karma Breakdown by Subreddit'),
]


class FetchDataForm(forms.Form):
    site_name = forms.CharField(label='Source Site', widget=forms.Select(choices=SOCIAL_MEDIA_SITES))
    content_type = forms.CharField(label='Content Type', widget=forms.Select(choices=CONTENT_TYPES))
    site_user = forms.CharField(label='Username', max_length=20)
    instance_limit = forms.IntegerField(label='Maximum Content Instances', min_value=1, max_value=1000)


class CreateVisualizationForm(forms.Form):
    visualization_type = forms.CharField(label='Visualization Type', widget=forms.Select(choices=VIS_TYPES))
    dataset = forms.CharField(label='Dataset User', max_length=20)
