from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


# http://127.0.0.1:8000/members
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


# http://127.0.0.1:8000/members/details/1
def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


# http://127.0.0.1:8000/
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def categories(request):
    template = loader.get_template('categories.html')
    context = {
        'categories': ['Telewizory', 'Telefony', 'Komputery', 'Lampy']
    }
    return HttpResponse(template.render(context, request))