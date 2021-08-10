from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)

    content = models.TextField(null=False)      #장문의 글을 받을때
                                                                        #짧은글은 charfield

    created_at = models.DateTimeField(auto_now_add=True)
