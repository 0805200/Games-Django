from django.shortcuts import render
from charactersapp.models import GameCharacter

def charsPage(request):
    allObjects = GameCharacter.objects.all()
    enemy = {"enemies":allObjects}
    return render(request, "all.chars.html", enemy)

def CurrentCharacter(request):
    return "Current character"
