from django.shortcuts import render
from .models import Block
from message.models import Message
from article.models import Article


def index(request):
    blocks = Block.objects.all()
    if not request.user.is_authenticated:
        return render(request, "blog/index.html", {"blocks": blocks})
    msg_cnt = Message.objects.filter(owner=request.user,status=1).count()
    article_list = Article.objects.filter(status=0).order_by("-create_timestamp")[:5]
    return render(request, 'blog/index.html', {'blocks': blocks,
                                               'msg_cnt': msg_cnt,
                                               'article_list':article_list})
