from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from welcomeApp.views import initPage, aboutPage
from charactersapp.views import charsPage, CurrentCharacter

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", initPage),
    path('about/', aboutPage, name = "about_path"),
    path("characters/", charsPage, name = "name"),
    path('currentCharacter/<str:charName>', CurrentCharacter, name = "current_characters")

]

if settings: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)