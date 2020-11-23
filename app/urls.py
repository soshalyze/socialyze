from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch/', views.fetch_new_social_data, name='fetch_new_social_data'),
    path('visualize/', views.choose_viz, name='choose_viz'),
]
