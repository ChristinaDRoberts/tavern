from django.db import models


class Lunch(models.Model):
    nickname = models.CharField(max_length = 150)
    user = models.CharField(max_length = 150)
    date = models.CharField(max_length = 150)



    def __str__(self):
        return self.nickname



class Location(models.Model):
    lunch = models.ForeignKey('Lunch', on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname