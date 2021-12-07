from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def blog_home(request,cat_name=None):
    posts=Post.objects.filter(status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    post=get_object_or_404(Post,id=pid,status=1)
    context={'post':post}
    return render(request,'blog/blog-single.html',context)
