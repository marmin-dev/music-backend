from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=200, null=False)
    username = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.username
