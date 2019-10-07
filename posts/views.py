from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Topic
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
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts':posts,
    }
    return render(request, 'tech-index.html', context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
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


def update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CreatePostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form':form,
    }
    return render(request, 'tech-create.html', context)

def topic(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    posts = topic.get_posts
    context = {
        'topic':topic,
        'posts':posts,
    }
    return render(request, 'tech-category-01.html', context)
