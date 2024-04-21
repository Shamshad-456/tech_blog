from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    amazon_affiliate_link = models.URLField()
    image_url = models.URLField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.created_at} on {self.article.title}"


class LikeDislike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes_dislikes')
    is_like = models.BooleanField()

    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.is_like:
            self.like_count += 1
        else:
            self.dislike_count += 1
        super(LikeDislike, self).save(*args, **kwargs)

    def __str__(self):
        return f"{'Like' if self.is_like else 'Dislike'} on {self.article.title}"
