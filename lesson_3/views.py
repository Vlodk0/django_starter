from django.http import HttpResponse, FileResponse, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse
from django.templatetags.static import static
from django.shortcuts import render

from django.views import View

from django.template import loader

# Create your views here.

class MyView(View):

    def get(self, request):
        if request.GET.get('type') == "file":
            FileResponse(open(static('img/001.jpg'), "rb+"))
        elif request.GET.get('type') == "json":
            JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
        elif request.GET.get('type') == "redirect":
            HttpResponseRedirect("http://www.google.com")
        else:
            HttpResponseNotAllowed('You shall not pass!!!')
        print(request.GET)
        return HttpResponse('This is GET')

    def post(self, request):
        print(request.POST)
        return HttpResponse('This is POST')

def main(request):
    # return HttpResponse("<button>Some button</button>")
    # test_template = loader.get_template(template_name='templates_example.html')
    # test_template_list = loader.select_template(template_name_list=["test",
    #                                                                 'templates_example.html'])
    # print(test_template_list)
    # return render(request, "templates_example.html")
    # return HttpResponse(test_template_list.render())
    test_template = loader.render_to_string('templates_example.html',
                                                 context={"str": "Test string",
                                                          "int": 10})
    return HttpResponse(test_template)


def text(request):
    return HttpResponse("This is text from backend to user interface")

def file(request):
    print(static('img/001.jpg'))
    return FileResponse(open(static('img/001.jpg'), "rb+"))

def redirect(request):
    return HttpResponseRedirect("http://www.google.com")

def not_allowed(request):
    return HttpResponseNotAllowed('You shall not pass!!!')

def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
