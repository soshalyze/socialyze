from app.models import RedditUser, RedditComment
import plotly.express as px
from plotly.offline import plot


def create_comment_bar_graph(username):
    user = RedditUser.objects.get(username=username)
    karma_dict = RedditComment.objects.get_comment_karma_by_sub(user)
    x_subs = list(sorted(karma_dict.keys()))
    y_karm = [karma_dict[sub] for sub in x_subs]
    fig = px.bar(x=x_subs, y=y_karm, labels={
        'x': 'Subreddit Name',
        'y': 'Cumulative Comment Karma',
        'title': 'Comment Karma Breakdown for /u/{}'.format(username)
    })
    plt = plot(fig, output_type='div', include_plotlyjs=False)
    return plt
