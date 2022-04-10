from django.shortcuts import render
from charactersapp.models import GameCharacter

def charsPage(request):
    allObjects = GameCharacter.objects.all()
    enemy = {"enemies":allObjects}
    return render(request, "all.chars.html", enemy)

def CurrentCharacter(request, charName):
    selected = GameCharacter.objects.all().filter(characterName = charName)
    character = selected[0]
    parametr = {"key_character" : character} 
    return render(request, "single_character.html", parametr)


