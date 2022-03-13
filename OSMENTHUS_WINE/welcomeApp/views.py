from django.http import HttpResponse
from django.shortcuts import render

def initPage(request): 
    return render(request, "index.html")


def aboutPage(request):
    return HttpResponse("Amogus! tu tu tu tu tu tu tu-tu")