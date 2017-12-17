from django.shortcuts import redirect
from .models import Article
from blog.models import Block
from .forms import ArticleForm
from django.shortcuts import render
from article.paginator import paginate_queryset
from django.contrib.auth.decorators import login_required
from comment.models import Comment


def article_list(request, block_id):
    block_id = int(block_id)
    # block = get_object_or_404(Block, id=block_id)
    block = Block.objects.get(id=block_id)
    all_article = Article.objects.filter(block=block, status=0).order_by("-id")
    page_no = int(request.GET.get("page_no","1"))
    page_articles, pagination_data = paginate_queryset(all_article, page_no)
    return render(request, "article/article_list.html",
                  {"articles": page_articles, "b": block,
                   "pagination_data":pagination_data})


def article_detail(request,article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    page_no = int(request.GET.get("pang_no", "1"))
    all_comment = Comment.objects.filter(article=article, status=0).order_by("-id")
    page_articles, pagination_data = paginate_queryset(all_comment, page_no)
    return render(request, "article/article_detail.html", {"article": article,
                                                           'comments':page_articles,
                                                           'pagination_data':pagination_data})


@login_required
def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "POST":
        user = request.user
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.block = block
            article.status = 0
            article.owner = user
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:
            return render(request, "article/article_create.html",
                                   {'b': block, 'form': article_form})
    return render(request, "article/article_create.html",
                           {'b': block})
