from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    superv = models.TextField()
    coment = models.TextField()
    # image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'글 번호 :{self.id}'
        
