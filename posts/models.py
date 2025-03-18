from django.db import models

# Create your models here.

class post(models.Model): # 클래스를 만들때 단수로 만든 이유 : 여러개의 포스트를 만드는 것이 아닌 포스트를 정의하는 것 ! 
    title = models.CharField(max_length=100) # 글자를 저장하는 필드 / TextField : 더 많은 양의 글자를 쓰는 경우 
    content = models.TextField()
