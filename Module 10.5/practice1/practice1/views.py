from django.http import HttpResponse

def home(response):
    return HttpResponse('<h1> Welcome To Django-Practice_Day01</h1>')
