from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=31, unique=True)
    email = models.CharField(max_length=63, unique=True)
    password = models.CharField(max_length=31)

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'email': self.email,
        }

