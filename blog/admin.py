from django.contrib import admin
from .models import Post,Category,Comment,Contact
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    list_display=('title','status','counted_views','published_date','created_date')
    list_filter=('status',)
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('name','post','approved','created_date')
    list_filter = ('post','approved',)
    search_fields=['name','post']

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display=('name','email','subject','created_date')


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Contact,ContactAdmin)
