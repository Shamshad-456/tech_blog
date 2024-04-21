import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import user_passes_test
from .models import Article, Comment, LikeDislike

@require_http_methods(["GET"])
def get_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    like_count = LikeDislike.objects.filter(article=article, is_like=True).count()
    dislike_count = LikeDislike.objects.filter(article=article, is_like=False).count()

    return JsonResponse({"article": {
        "id": article.id,
        "title": article.title,
        "content": article.content,
        "publish_date": article.publish_date,
        "amazon_affiliate_link": article.amazon_affiliate_link,
        "image_url": article.image_url,
        "like_count": like_count,
        "dislike_count": dislike_count,
    }})

@require_http_methods(["GET"])
def get_all_articles(request):
    articles = Article.objects.all()
    articles_list = [{"id": article.id, "title": article.title,"image_url":article.image_url} for article in articles]
    return JsonResponse({"articles": articles_list})


@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["POST"])
def post_article(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    amazon_affiliate_link = request.POST.get("amazon_affiliate_link")
    image_url = request.POST.get("image_url")
    article = Article.objects.create(title=title, content=content, amazon_affiliate_link=amazon_affiliate_link, image_url=image_url)
    return JsonResponse({"article_id": article.id})


@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["PUT"])
def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.title = request.POST.get("title", article.title)
    article.content = request.POST.get("content", article.content)
    article.amazon_affiliate_link = request.POST.get("amazon_affiliate_link", article.amazon_affiliate_link)
    article.image_url = request.POST.get("image_url", article.image_url)
    article.save()
    return JsonResponse({"message": "Article updated successfully"})

@csrf_exempt
@require_http_methods(["POST"])
def post_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    content = request.POST.get("content")
    comment = Comment.objects.create(article=article, content=content)
    return JsonResponse({"comment_id": comment.id})

@csrf_exempt
@require_http_methods(["PUT"])
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.content = request.POST.get("content", comment.content)
    comment.save()
    return JsonResponse({"message": "Comment updated successfully"})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return JsonResponse({"message": "Comment deleted successfully"})

@require_http_methods(["GET"])
def get_comments(request, article_id):
    comments = Comment.objects.filter(article_id=article_id)
    comments_list = [{"id": comment.id, "content": comment.content, "created_at": comment.created_at} for comment in comments]
    return JsonResponse({"comments": comments_list})

@csrf_exempt
@require_http_methods(["POST"])
def like_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    like, created = LikeDislike.objects.get_or_create(article=article, is_like=True)
    if not created:
        like.delete()
    return JsonResponse({'status': 'success'})

@csrf_exempt
@require_http_methods(["POST"])
def dislike_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    dislike, created = LikeDislike.objects.get_or_create(article=article, is_like=False)
    if not created:
        dislike.delete()
    return JsonResponse({'status': 'success'})

