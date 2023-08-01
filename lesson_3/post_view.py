from django.http import HttpResponse
from django.template import loader

from django.views.generic import TemplateView


class MyTemplateView(TemplateView):
    template_name = 'post_page.html'

    def get_context_data(self, **kwargs):
        return {'latest_question_list': [{'id': 1,
                                          'question_text': 'Бути чи не бути?'},
                                         {'id': 2,
                                          'question_text': 'Boxer or wrestler?'},
                                         {'id': 3,
                                          'question_text': 'Russia is parasha?'},
                                         {'id': 4,
                                          'question_text': 'Russia is terrorist?'},
                                         {'id': 5,
                                          'question_text': None}]}


# def index_post(request):
#     latest_question_list =
#     template = loader.get_template('post_page.html')
#     context = {'latest_question_list': latest_question_list}
#     return HttpResponse(template.render(context, request))

def post_page(request, number):
    if number == 1:
        return HttpResponse('Слова з монологу Гамлета, героя трагедії "Гамлет, принц Датський" (1601) великого '
                            'англійського драматурга В. Шекспіра. У переносному вживанні означають: найважливіше '
                            'питання, питання життя і смерті.')
    elif number == 2:
        return HttpResponse('The answer depends on many factors, but its fair to say that wrestlers have better '
                            'chances of beating boxers. Of course, there are hundreds of different scenarios where '
                            'the fight can go both ways. But overall, wrestlers are superior to boxers for one simple '
                            'reason')
    elif number == 3:
        return HttpResponse('Yes, 100%')
    else:
        return HttpResponse('Another question!!!')
