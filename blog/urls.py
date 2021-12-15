from .views import *
from django.urls import path
from blog.feeds import LatestEntriesFeed

app_name="blog"
urlpatterns= [
            path('',blog_home,name='blog_home'),
            path('single',blog_single,name='blog_single'),
            path('<int:pid>',blog_single,name='single'),
            path('category/<str:cat_name>',blog_home,name='category'),
            path('author/<str:author_name>',blog_home,name='author'),
            path('search/',blog_search,name='search'),
            path('rss/feed/', LatestEntriesFeed()),    
]
