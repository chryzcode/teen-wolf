from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=400)
    message = models.TextField()

    def __str__(self):
        return self.name
