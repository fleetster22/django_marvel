from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404

from marvel import Marvel

from .models import Characters


def list_characters(request):
    char_list = get_list_or_404(Characters)
    context = {"char_list": char_list}
    return render(request, "characters/list.html", context)


def show_character(request, name):
    character = Characters.objects.get(name=name)
    context = {"character": character}
    return render(request, "characters/character.html", context)
