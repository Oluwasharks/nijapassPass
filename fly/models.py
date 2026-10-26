from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=100, default="Lagos")
    price = models.IntegerField(default=0)
    image_url = models.URLField(default="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title