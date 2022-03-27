from django.shortcuts import render

def charsPage(request): 
    return render(request, "all.chars.html")
