from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Koment(models.Model):
    name = models.CharField(max_length=25)
    koment = models.TextField()
    data = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class Hleb(models.Model):
    description = models.CharField(max_length=100)
    button= models.CharField(max_length=10)
    img = models.FileField(upload_to='./static/')

    def __str__(self):
        return str(self.button)

class Proba(models.Model):

    o = models.TextField()

class Hleba(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    kratk = models.CharField(max_length=80)
    button= models.CharField(max_length=12)
    img = models.FileField(upload_to='./static/')

    def __str__(self):
        return str(self.name)