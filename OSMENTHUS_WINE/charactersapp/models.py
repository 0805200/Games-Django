from email.base64mime import header_length
from unicodedata import name
from xml.dom.domreg import well_known_implementations
from xml.dom.minidom import Element
from django.db import models

class GameCharacter(models.Model):
    characterName = models.CharField(max_length = 20)
    damage = models.IntegerField()
    health = models.IntegerField()
    high = models.IntegerField()
    weapon = models.CharField(max_length = 10)
    element = models.CharField(max_length = 10)
    birthday = models.IntegerField()
    charBirthday = models.DateField(default="1984-05-05")
    c = models.CharField(max_length = 20)
    avatar = models.ImageField(blank = True)



