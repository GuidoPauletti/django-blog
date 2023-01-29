from django.urls import path
from .views import render_posts, render_single_post

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', render_single_post, name='single_post'),
]