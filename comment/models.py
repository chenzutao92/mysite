from django.db import models
from django.contrib.auth.models import User
from article.models import Article


class Comment(models.Model):
    owner = models.ForeignKey(User,verbose_name="作者")
    article = models.ForeignKey(Article,verbose_name="文章")
    to_comment = models.ForeignKey("self", null=True,
                                   blank=True, verbose_name="被回复的评论")
    content = models.CharField("评论内容",max_length=140)
    status = models.IntegerField('状态',choices=((0,'正常'),(1,'删除')))
    create_timestamp = models.DateTimeField('创建时间', auto_now_add=True)
    last_update_timestamp = models.DateTimeField('最后更新时间', auto_now=True)

    def __str__(self):
        return self.owner

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'


