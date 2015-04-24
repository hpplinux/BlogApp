from django.contrib import admin
from blogs.models import Blog, User, Comment


admin.site.register(Blog)
admin.site.register(User)
admin.site.register(Comment)
