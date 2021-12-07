from django.contrib import admin
from .models import Post,Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display=('title','status','counted_views','published_date','created_date')
    list_filter=('status',)


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
