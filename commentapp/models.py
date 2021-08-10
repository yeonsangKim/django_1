
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True) #on_delete=models.SET_NULL는 WIRTER가 탈퇴했을때
                                                                                            #게시글은 유지되면서 WRITER가 NULL로 바뀜
                                                                                            #CASCADE는 게시글 자체가 없어짐
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)
    content = models.TextField(null=False)      #장문의 글을 받을때
                                                                        #짧은글은 charfield

    created_at = models.DateTimeField(auto_now_add=True)