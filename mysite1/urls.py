from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include, re_path
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from django.contrib.auth import views as auth_views

sitemaps={'static':StaticViewSitemap,'blog':BlogSitemap,}

app_name="mysite1"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('elements/',elements,name='elements'),
    path('contact/',contact,name='contact'),
    path('blog/',include('blog.urls')),
    path('summernote/',include('django_summernote.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',include('robots.urls')),
    path('accounts/', include('allauth.urls')),
    # re_path(r"^.*",maintenance),
    re_path(r'^password-reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
