from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'articles/index.html')


def greeting(request):
    foods = ['apple', 'banana', 'cocount', ]
    info = {
        'name': 'Alice',
    }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'articles/greeting.html', context)


def new(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    addr = request.GET.get('addr')

    context = {
        'name': name,
        'age': age,
        'addr': addr,
    }
    return render(request, 'articles/new.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    message = request.GET.get('throw')

    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)
