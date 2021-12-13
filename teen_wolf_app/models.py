from django.db import models

# Create your models here.
class ContactForm(models.Model):
    title = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=400)
    content = models.TextField()

    def __str__(self):
        return self.name
