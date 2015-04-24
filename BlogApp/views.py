from django.shortcuts import render_to_response
from blogs.models import Blog, User, Comment
from BlogApp.forms import UserInfo
from datetime import datetime
from django.core.context_processors import csrf
from django.template import RequestContext
#from django.http import HttpResponse




def blogs(request):
    blog = Blog.objects.all()
    return render_to_response('blogs.html', {'blogs': blog})# dict argurement which from db.

def blog(request, id):
    id = int(id)
    blog = Blog.objects.get(id=id) # get the id from url.
    comment = Comment.objects.filter(blog_id=id) # ??Is there any problem?

    if request.method == 'POST':
        #form = UserInfo(request.POST)
        #user = User(form.name, form.email, form.website)
        #user.save()
    #exception
        #now = datetime.now()
        #comment = Comment(user, blog, form.comment, now)
        #comment.save()
        c = RequestContext(request, {'blog': blog, 'comments': comment })
        return render_to_response('blog.html', c)
    return render_to_response('blog.html', {'blog': blog, 'comments': comment})# To invoke insert func there.
    #if request.method == 'POST':
    #form = UserInfo(request.POST)
        #if form.is_valid():
    #create_comments = form.cleaned_data
        # else, there is a except
    #return render_to_response('blog.html', {'blog': blog, 'comments':comment, 'form': create_comments })# form to deal with User Comment.
    #else: # There are some problem with create comments.
    #    raise BaseException

def about(request):
    return render_to_response('about.html')# There to define other function to
                                           # be invoked by this view functions.
