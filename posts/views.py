from django.shortcuts import render
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