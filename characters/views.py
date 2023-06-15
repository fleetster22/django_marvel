from django.http import JsonResponse
from django.shortcuts import render
import hashlib
import datetime
import requests
from marvel import Marvel

from .models import Characters
from characters.serializers import CharacterSerializer
from keys import PRIVATE_KEY, PUBLIC_KEY

timestamp = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")


def hash_params():
    hash_md5 = hashlib.md5()
    hash_md5.update(f"{timestamp}{PRIVATE_KEY}{PUBLIC_KEY}".encode("utf-8"))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


params = {"ts": timestamp, "apikey": PUBLIC_KEY, "hash": hash_params()}
res = requests.get("https://gateway.marvel.com:443/v1/public/characters", params=params)


def character_list(request):
    characters = Characters.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return JsonResponse(serializer.data)


def show_character(request, name):
    character = Characters.objects.get(name=name)
    context = {"character": character}
    return render(request, "characters/character.html", context)
