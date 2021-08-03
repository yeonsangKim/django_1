from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):            #게시글
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                             related_name='article',null=True)      #User  vs 다 로 연결시켜줌, SET_NULL= 작성자 비공개

    title =  models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/',null=True)  #media파일에 article 폴더에 이미지 저장
    content = models.TextField(null=True)


    created_at = models.DateField(auto_now_add=True)     #db가 작성된 시간이 자동으로 저장
