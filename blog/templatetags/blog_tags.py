from django import template
from article.models import Article
from django.db.models import Count


register = template.Library()


@register.simple_tag
def total_article():
    return Article.objects.filter(status=0).count()


@register.inclusion_tag('blog/index.html')
def show_latest_article(count=5):
    latest_article = Article.objects.filter(status=0).order_by("-create_timestamp")[:count]
    return {'latest_article': latest_article}


@register.assignment_tag
def get_most_commented_article(count=5):
    return Article.objects.filter(status=0).annotate(
                total_comments=Count('comment')
            ).order_by('-total_comments')[:count]

