from django.contrib import admin

from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/<int:article_id>/', views.get_article, name='get_article'),
    path('articles/', views.get_all_articles, name='get_all_articles'),
    path('article/', views.post_article, name='post_article'),
    path('article/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('article/<int:article_id>/comments/', views.get_comments, name='get_comments'),
    path('article/<int:article_id>/comment/', views.post_comment, name='post_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('article/<int:article_id>/like/', views.like_article, name='like_article'),
    path('article/<int:article_id>/dislike/', views.dislike_article, name='dislike_article'),
]
