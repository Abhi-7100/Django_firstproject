from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    age = models.IntegerField()
    terms_and_conditions = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
