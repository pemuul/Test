from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
# Если в activ инициализировать gl(главная), re(расчёт), o(о нас), то они появяться выделеныим на hedore
from django.views.decorators.csrf import csrf_exempt

from task.models import Name, Hleba, Proba, Koment


def home(self):
    return HttpResponse("dddd")


def index(request):
    mail = {
        'autorizait': 'войти',
        'activ': {'gl': '1',
                  're': '',
                  'o': ''},
        'f':[0, 1, 2],
        'all': Hleba.objects.all(),
        'range': list(range(1, 31, 3)),
        'range2': list(range(3, 34, 3)),
    }
    return render(request, 'main.html', mail)


def rashot(request):
    mail = {'autorizait': 'войти', 'activ': {'re': '1',}}
    return render(request, 'rashot.html', mail)


def o_nas(request):
    # name = Name(name="Roma", age="18")
    # name.save()
    d = str(datetime.datetime.now())
    print(d[11:19])
    h = Koment.objects.all()
    mail = {'autorizait': 'войти', 'activ': {'o': '1'}, 'names': h}
    return render(request, 'o_nas.html', mail)


@csrf_exempt
def csrf(request):
    name = request.POST["name"]
    koment = request.POST["age"]
    d = str(datetime.datetime.now())
    print(d[11:19])
    try:
        if not Koment.objects.filter(name=name):
            new = Koment(name=name, koment=koment, data=d[11:16]+" "+d[8:10]+"."+d[5:7]+"."+d[0:4])
            #print(d[11:18])
            new.save()
            return HttpResponse("Ok")
        else:
            return HttpResponse("No")
    except:
        print("Ошибка")
        return HttpResponse("Ошибка")


def main(request, slug):
    slu = slug[6:]
    g = Hleba.objects.all()
    mail = {'autorizait': 'войти', 'activ': {'rash':slug},
            'head':str(g[int(slug) - 1]),
            'content':str(g[int(slug)-1]),
            'content2':str(g[int(slug)-1].description),
            'img': str(g[int(slug) - 1].img),
            }
    return render(request, 'rashot.html', mail)