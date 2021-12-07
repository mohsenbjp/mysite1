from django import template
register=template.Library()
from blog.models import Post,Category

@register.inclusion_tag('blog/blog-latestpost.html')
def latestpost(a=3):
    latestpost=Post.objects.filter(status=1).order_by('published_date')[:a]
    return {'latestpost':latestpost}

@register.inclusion_tag('blog/blog-category.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    categories=Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}
