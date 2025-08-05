from django.db import models

class article(models.Model):
    TYPE_CHOICES = [
        ('P', 'products'),
        ('S', 'Services'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title