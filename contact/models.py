from django.db import models
from django.utils import timezone

class ContactModel(models.Model):
    first_name = models.CharField( max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)                    
    # category = models.ForeignKey()
    show = models.BooleanField(default=True)
    # owner = models.ForeignKey()
    picture = models.ImageField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
