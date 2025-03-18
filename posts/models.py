from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=100) # 글자를 저장하는 필드 / TextField : 더 많은 양의 글자를 쓰는 경우 
    content = models.TextField()
