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

    post = Post() # 새로운 정보를 만듦.
    post.title = title  # 전자 : models.py에서 만든 title / 후자 : request.GET에서 가져온 title 
    post.content = content
    post.save()       # id를 만들어줌 

  #  return redirect('/index/') # 게시물 생성 후 index로 이동 (어디로 가야 할지 경로 설정)
    return redirect(f'/posts/{post.id}/') 

def delete(request,id):
    post = Post.objects.get(id=id) # 1. 게시물 찾기
    post.delete() # 2. 게시물 삭제

    return redirect('/posts/') # 삭제됐으므로 인덱스로 이동


def edit(request,id):
    post = Post.objects.get(id=id)

    context = {
        'post':post,
    }
    return render(request, 'edit.html', context)

def update(request, id): 
    # 기존 정보 가져오기
    post = Post.objects.get(id=id)
    # 새로운 정보 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 기존 정보를 새로운 정보로 수정하기
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')
    