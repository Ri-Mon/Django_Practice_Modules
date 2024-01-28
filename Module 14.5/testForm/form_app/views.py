from django.shortcuts import render
from . forms import TestForm

def django_form(request):
    form = TestForm()
    return render(request, 'form.html', {'form': form})