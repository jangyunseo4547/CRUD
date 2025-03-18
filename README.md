# crud

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

- 앱 등록 (setting)
```shell
INSTALLED_APPS = 
...
'posts' # 적어주기 
```