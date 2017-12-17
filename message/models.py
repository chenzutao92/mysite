from django.db import models
from django.contrib.auth.models import User
from comment.models import Comment


class Message(models.Model):
    owner = models.ForeignKey(User,verbose_name="作者")
    content = models.CharField("回复内容",max_length=100)
    link = models.CharField("链接",max_length=1000)
    status = models.IntegerField('状态',choices=((0,'已查看'),(1,'未查看')))
