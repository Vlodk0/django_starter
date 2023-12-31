import datetime

from django.db import models


# Create your models here.
class GameModel(models.Model):
    name = models.CharField(max_length=64)
    platform = models.CharField(max_length=64)
    year = models.DateField(default=datetime.date(2000, 1, 1))
    genre = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    na_sales = models.FloatField(default=1.0)
    eu_sales = models.FloatField(default=1.0)
    jp_sales = models.FloatField(default=1.0)
    other_sales = models.FloatField(default=1.0)
    global_sales = models.FloatField(default=1.0)

    def __str__(self):
        return f"{self.id}_{self.name}"


class GamerLibraryModel(models.Model):
    game = models.ManyToManyField("GameModel")
    gamer = models.ForeignKey("GamerModel", on_delete=models.DO_NOTHING)
    size = models.IntegerField()

    def __str__(self):
        return f"{self.id}_{self.gamer.nickname}"


class GamerModel(models.Model):
    nickname = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id}_{self.nickname}"