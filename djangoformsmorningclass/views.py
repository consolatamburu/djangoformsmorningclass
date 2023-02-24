from django.shortcuts import render
from djangoformsmorningclass.forms import studentform


def index(request):
    student = studentform()
    return render(request, 'index.html', {'form': student})


