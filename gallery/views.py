from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request, 'gallery.html', {})


def detail(request, question_id):
    question = question_id
    if question < 1:
        question = 1
    return render(request, 'detail.html', {'question': question})
