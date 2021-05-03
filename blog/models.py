from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.post.title} {self.name} '