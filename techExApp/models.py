from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    nation = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name