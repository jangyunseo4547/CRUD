# crud
- create : 생성
- read : 읽기 or (연출)
- update : 갱신
- delete : 삭제

### orm : 객체 관계 매핑


## 0. setting
- python -m venv venv
- source venv/Scripts/activate
- gitignore 설정 (장고, 파이썬, 윈도우, 맥)

## 1. django 설정
- pip install django

- 프로젝트 생성
```shell
django-admin startproject crud .
```

- 앱 생성
```shell
django-admin startapp posts # 앱 이름 : posts
```

- 앱 등록 (`setting`)
```shell
INSTALLED_APPS = 
...
'posts' # 적어주기 
```

- (`urls.py`)
```python
from posts import views # views를 불러와야 views.~ 사용 가능
path('index/', views.index),
```

- (`views.py`)
```python
def index(request):
    return render(request, 'index.html')
```

- posts에 `templates` 폴더 생성!! -> html 파일 만들기

## 2. CRUD

- `modeling` 
- skema 정의 (데이터 정의, 설계) - (`model.py`)
```python 
class post(models.Model):
    title = models.CharField(max_length=100) 
    # CharField : 글자를 저장하는 필드
    content = models.TextField() 
    # TextField : 더 많은 양의 글자를 쓰는 경우 
```

- `migration`
- python --> sql(`db.sqlite3`)로 이주
```shell
# 번역본 생성
python manage.py makemigrations
```

```shell
# DB에 반영
python manage.py migrate
## Apply all migrations: admin, auth, contenttypes, posts, sessions : posts외의 장고에서 이미 만들어진 파일도 이주함. 
```

- extention에서 sqlite viewer 설치 
    - db.sqlite3가 핑크색으로 바뀜 
    - `posts_post` 확인 시 title, content, id 생성됨.

- create super user 
```shell
# admin의 관리자 페이지 id, pw 만들기
python manage.py createsuperuser
```

- (`admin.py`)에 Post 추가 등록
```python
from .models import Post #model.py에 있는 post 사용
admin.site.register(Post) # admin에 post를 추가 등록
```

- (`views.py`) 전체 데이터 & 단일 게시글 불러오기 
```python
from .models import Post

def index(request):
    posts = Post.objects.all() # Post 대문자

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
```

- (`detail.py`)에 링크 달어 접근하기