from django.shortcuts import render
from django.http import HttpResponse
from garn.yarnjournal.models import StashEntry


def index(request):
    stash=StashEntry.objects.all()
    length = 1/3
    kilos = 0
    for entry in stash:
        length = length + entry.weight * entry.yarn.meterage/100
        kilos = kilos + entry.weight/1000
    return HttpResponse(f"I have {length:.2f} meters of yarn in my stash. \n That equals {kilos:.2f} kg.")
