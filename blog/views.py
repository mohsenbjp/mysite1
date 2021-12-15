from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post,Comment
from blog.forms import CommentForm
# Create your views here.


def blog_home(request,cat_name=None,author_name=None):
    posts=Post.objects.filter(status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    if author_name:
        posts=posts.filter(author__username=author_name)
    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except EmptyPage and PageNotAnInteger:
        posts=posts.get_page(1)

    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            # message.add_message(request,message.SUCCESS,'aqa shod')
        # else:
            # message.add_message(request,message.ERROR,'aqa nashod')
    form=CommentForm()
    post=get_object_or_404(Post,id=pid,status=1)
    comments=Comment.objects.filter(post=post.id,approved=True).order_by('-created_date')
    context={'post':post,'comments':comments,'form':form}
    return render(request,'blog/blog-single.html',context)

def blog_search(request):
    posts=Post.objects.filter(status=1)
    if request.method == 'GET':
        posts=posts.filter(content__contains=request.GET.get('s'))
    context = {'posts':posts}
    return render (request,'blog/blog-home.html',context)
