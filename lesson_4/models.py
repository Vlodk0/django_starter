from django.db import models
from datetime import timedelta

from django.contrib.auth.models import User


class Flower(models.Model):
    count = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(null=True)
    delivered_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    could_use_in_bouquet = models.BooleanField(default=True, null=True)
    wiki_page = models.URLField(default='https://www.wikipedia.org/', name='wikipedia', unique_for_date='delivered_at',
                                null=True)
    name = models.CharField(max_length=64, unique=True, null=True)


class Bouquet(models.Model):
    shop = models.Manager()
    fresh_period = models.DurationField(default=timedelta(days=5), help_text='Use this field when you need to have '
                                                                             'information about bouquet fresh time',
                                        null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=1.0, null=True)
    flowers = models.ManyToManyField(Flower, verbose_name='This bouquet consists of these flowers')


class Client(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    name = models.CharField(max_length=64, null=True)
    invoice = models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')
    user_uuid = models.UUIDField(editable=False, null=True)
    discount_size = models.DecimalField(decimal_places=5, max_digits=5, null=True)
    client_ip = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')


    def __str__(self):
        return self.name
