from django.conf.urls import include, url

from users.views import dashboard, register
import app.views as appviews

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^register/', register, name='register'),
    url(r'^app/fetch/', appviews.fetch_new_social_data, name='fetch'),
    url(r'^app/visualize/', appviews.choose_viz, name='visualize'),
]
