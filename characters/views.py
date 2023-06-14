from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404

from marvel import Marvel
from keys import PRIVATE_KEY, PUBLIC_KEY

from .models import Characters


def show_character(request, id):
    character = Characters.objects.get(id=id)
    context = {"character": character}
    return render(request, character.html, context)
