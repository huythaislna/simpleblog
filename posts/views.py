from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post
from .forms import CreatePostForm
# Create your views here.

def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    context = {
        'posts':posts,
    }
    return render(request, 'tech-index.html', context)

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post':post,
    }
    return render(request, 'tech-single.html', context)

def create(request):
    form = CreatePostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form':form,
    }
    return render(request, 'tech-create.html', context)


def update(request, id):
    post = get_object_or_404(Post, id=id)
    form = CreatePostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form':form,
    }
    return render(request, 'tech-create.html', context)

