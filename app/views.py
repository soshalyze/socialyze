from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from app.forms import FetchDataForm, CreateVisualizationForm
from app.reddit_comm import RedditCommunication
from app.models import RedditUser
import app.visualizations


def index(request):
    return HttpResponse("Hello, world. This is the socialyze app index.")


@login_required
def fetch_new_social_data(request):
    if request.method == 'POST':
        form = FetchDataForm(request.POST)
        if form.is_valid():
            reddit_user = form.cleaned_data['site_user']
            content_type = form.cleaned_data['content_type']
            instance_limit = form.cleaned_data['instance_limit']

            if RedditUser.objects.app_user_has_reddit_user(request.user, reddit_user):
                print('user {} already has the data for account {}'.format(request.user.username, reddit_user))
                return HttpResponseRedirect('/app/visualize/')
            elif RedditUser.objects.reddit_user_exists(reddit_user):
                print('linking user {} to existing data for account {}'.format(request.user.username, reddit_user))
                RedditUser(request.user, reddit_user).save()
                return HttpResponseRedirect('/app/visualize/')

            # TODO: If more than the previously downloaded instance count is fetched, actually fetch it
            comm = RedditCommunication(request.user, reddit_user)
            if content_type == 'post':
                comm.fetch_posts(instance_limit)
                print('fetching posts, instance limit {}'.format(instance_limit))
            elif content_type == 'comment':
                comm.fetch_comments(instance_limit)
                print('fetching comments, instance limit {}'.format(instance_limit))
            return HttpResponseRedirect('/app/visualize/')
    else:
        return render(request, 'fetchdata.html', {'form': FetchDataForm()})


@login_required
def choose_viz(request):
    if request.method == 'GET':
        return render(request, 'chooseviz.html', {'form': CreateVisualizationForm()})
    elif request.method == 'POST':
        form = CreateVisualizationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['visualization_type'] == 'karma_by_sub':
                graph = app.visualizations.create_comment_bar_graph(form.cleaned_data['dataset'])
                return render(request, 'showviz.html', {'plot_div': graph})

@login_required
def sandbox(request):
    return render(request, 'sandbox.html')


