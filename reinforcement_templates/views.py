from django.http import HttpResponse
from django.shortcuts import render


def new_profile(request):
    context = {"info": ["email", "username", "pin", "website", "address", "alias"]}
    return HttpResponse(render(request, 'profiles/new.html', context))