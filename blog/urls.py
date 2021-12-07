from .views import *
from django.urls import path

app_name="blog"
urlpatterns= [
            path('',blog_home,name='blog_home'),
            path('single',blog_single,name='blog_single'),
            path('<int:pid>',blog_single,name='single'),
            path('category/<str:cat_name>',blog_home,name='category'),

]
