from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_article = Article.objects.get(pk=kwargs['pk'])   #db에서 뽑아온다
        if target_article.writer== request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated