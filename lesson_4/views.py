from decimal import Decimal
from uuid import uuid4

from django.core.files import File
from django.http import HttpResponse


from django.contrib.auth.models import User
from lesson_4.models import Flower, Bouquet, Client


# Create your views here.

def create_flower(request):
    rose = Flower()
    rose.count = 5
    rose.description = 'рід і культурна форма рослин родини трояндових, листопадні, рідко вічнозелені кущі до 4 ' \
                       'метрів заввишки. '
    rose.could_use_in_bouquet = True
    rose.wiki_page = 'https://uk.wikipedia.org/wiki/%D0%A2%D1%80%D0%BE%D1%8F%D0%BD%D0%B4%D0%B0'
    rose.name = 'Троянда'
    rose.save()
    return HttpResponse("Created!")


def create_client(request):
    # with open('requirements.txt', 'r') as _file:
    #     tmp_file = _file.read()

    client = Client.objects.create(**{
        'user': User.objects.get(pk=1),
        # 'email': 'admin@admin1.com',
        'email': 'adminadmin1.com',
        'name': 'MyName',
        'invoice': File(open('requirements.txt')),
        'user_uuid': uuid4(),
        'discount_size': Decimal("0.00052"),
        'client_ip': "192.0.2.1.",
        # password superuser: 123

    })
    return HttpResponse("Created!")


def get_flower(request):
    price = Bouquet.shop.get(id=1).price
    return HttpResponse(price)
