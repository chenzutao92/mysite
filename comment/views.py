from django.shortcuts import render,HttpResponse
from article.models import Article
from message.models import Message
import json
from comment.models import Comment
from django.contrib.auth.decorators import login_required


@login_required
def comment(request):
    if request.method == "POST":
        article_id = request.POST['article_id']
        content = request.POST['content'].strip()
        to_comment_id = int(request.POST.get("to_comment_id", 0))
        article = Article.objects.get(id=article_id)
        user = request.user
        if not content:
            return json_response({"status": "err", "msg": "内容不能为空"})
        if to_comment_id != 0:
            to_comment = Comment.objects.get(id=to_comment_id)
        else:
            to_comment = None
        c = Comment(owner=user, article=article, content=content, status=0, to_comment=to_comment)
        c.save()
        link = "http://%s/article/detail/%s" % (request.get_host(), article_id)
        print(link)
        contents = "有人评论你‘" + content + "'"
        m = Message(owner=user, content=contents, link=link, status=1)
        m.save()

        return json_response({"status": "ok", "msg": ""})
    else:
        return render(request, "article/article_detail.html")


def json_response(obj):
    txt = json.dumps(obj)
    return HttpResponse(txt)