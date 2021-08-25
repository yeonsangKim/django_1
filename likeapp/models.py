from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='like_record',null=False)

    article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name='like_record',null=False)

    class Meta :
        unique_together=['user','article']  #user와 article 의 쌍이 유니크하다.