from django.conf.urls import patterns
from BlogApp import views
#from BlogApp.views import index, blog, about
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', admin.site.urls),
    #(r'^index/$', views.index), # Use Blogs. And use admin to write new articles.
    (r'^blog/(\d)/$', views.blog), # Blog article, which include comments and to be comments. The comments need user information that in User class in models.
    (r'^blogs/$', views.blogs),
    (r'^about/$', views.about),# Static Page about Bloger.
)
