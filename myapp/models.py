from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Optional image upload field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
