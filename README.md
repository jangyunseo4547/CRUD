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

- modeling : skema 정의 (데이터 정의, 설계) - (`model.py`)
```python 
class post(models.Model):
    title = models.CharField(max_length=100) 
    # CharField : 글자를 저장하는 필드
    content = models.TextField() 
    # TextField : 더 많은 양의 글자를 쓰는 경우 
```

- migration
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


