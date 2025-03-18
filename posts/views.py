from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all() #게시글 전체 가져와서 html에 넣기

    context = {
        'posts':posts,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id) # 게시글 하나를 가져오기

    context = {
        'post':post,
    }
    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title  # 전자 : models.py에서 만든 title / 후자 : request.GET에서 가져온 title 
    post.content = content
    post.save()

  #  return redirect('/index/') # 게시물 생성 후 index로 이동 (어디로 가야 할지 경로 설정)
    return redirect(f'/posts/{post.id}/') 
