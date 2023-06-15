from django.contrib import admin
from characters.models import Characters


@admin.register(Characters)
class CharactersAdmin(admin.ModelAdmin):
    list_display = ("name", "char_id")
