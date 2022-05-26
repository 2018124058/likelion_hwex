from django.db import models
from django.utils import timezone

# Create your models here.
# 게시물
class Post(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(blank=True, null=True, upload_to='post_photo')
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# 댓글
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment