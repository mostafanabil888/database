from django.db import models

# Create your models here.
class User (models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=20)
    email=models.EmailField()

    def _str_(self) -> str:
        return self.id
    