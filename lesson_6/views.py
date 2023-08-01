import csv
import datetime

from django.http import HttpResponse
from django.views.generic import ListView

from lesson_6.models import GameModel, GamerModel, GamerLibraryModel
from django.db.models import Q


def upload_data(request):
    with open('vgsales.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            try:
                _, created = GameModel.objects.get_or_create(
                    name=row[1],
                    platform=row[2],
                    year=datetime.date(int(row[3]), 1, 1),
                    genre=row[4],
                    publisher=row[5],
                    na_sales=row[6],
                    eu_sales=row[7],
                    jp_sales=row[8],
                    other_sales=row[9],
                    global_sales=row[10],

                )
            except:
                pass
    return HttpResponse("Done")


class FilterView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name__contains="Hitman")


class ExcludeView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains="Hitman")


class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains="Hitman").order_by('year').reverse()


class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()


class UnionView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Hitman (2016)").union(GameModel.objects.filter(name='Tetris'))


class NoneView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.none()


class ValuesView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Hitman (2016)").values()

    def get(self, request, *args, **kwargs):
        print(list(
            GameModel.objects.filter(name="Hitman (2016)").values_type("name", "platform")))

        return super().get(request, *args, **kwargs)


def date_view(request):
    data = GameModel.objects.dates(field_name='year', kind='month')
    print(data)
    return HttpResponse(data)


def get_view(request):
    data = GameModel.objects.get(pk=1)
    print(data)
    return HttpResponse(data)


def create_view(request):
    myself = GamerModel()
    myself.email = "admin@admin.com"
    myself.nickname = "SomeRandomNickname"
    myself.save()

    # myself = GamerModel(email="admin@admin.com", nickname="SomeRandomNickname")
    # myself.save()

    # myself = GamerModel(**{"email": "admin@admin.com", "nickname": "SomeRandomNickname"})
    # myself.save()

    # myself = GamerModel.objects.create(**{"email": "admin@admin.com", "nickname": "SomeRandomNickname"})
    # myself = GamerModel.objects.create(email="admin@admin.com", nickname="SomeRandomNickname")
    # myself = GamerModel.objects.bulk_create([
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNickname"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNickname"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNickname")
    # ])

    # my_library = GamerLibraryModel(gamer=GamerModel.objects.get(pk=10), size=10)
    # my_library.save()
    # my_library.game.set([GameModel.objects.get(pk=1),
    #                      GameModel.objects.get(pk=2)])

    # my_library = GamerLibraryModel.objects.create(gamer=GamerModel.objects.get(pk=10), size=10)
    # my_library.game.set([GameModel.objects.get(pk=1),
    #                      GameModel.objects.get(pk=2)])

    # my_library = GamerLibraryModel.objects.bulk_create(
    #     [GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        game=[GameModel.objects.get(pk=1),
    #                        GameModel.objects.get(pk=1)], size=10),
    #      GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        game=[GameModel.objects.get(pk=1),
    #                              GameModel.objects.get(pk=1)], size=10)])

    # my_friend = GamerModel.objects.get(pk=10)
    # my_friend.nickname = "MyFriend"
    # # my_friend.update(nickname="MyFriend")
    # my_friend.save()
    return HttpResponse(myself)

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
# queryset = GameModel.objects.filter(
#     Q(name__startwith="A") & Q(name__endwith="a") & Q(name__contains="ma"))

# queryset = GameModel.objects.filter(
#     Q(name__startwith="A") & Q(name__endwith="a"))

# queryset = GameModel.objects.filter(
#     Q(name__startwith="Ab") | Q(name__startwith="Ad") | Q(name__startwith="Mat"))

# queryset = GameModel.objects.filter(
#     ~Q(name__startwith="Ab") | ~Q(name__startwith="Ad") | ~Q(name__startwith="Mat"))


# def relation_filter_view(request):
#     data = GamerLibraryModel.objects.filter(gamer__email__contains="a")
#     print(data[0].gamer.email)
#     # return HttpResponse(data)
#     return HttpResponse(data.order_by())
