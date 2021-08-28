from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view


def home(request):
    return render(request, 'home.html')


@api_view(["GET","POST"])
def form(request):
    if request.method=="POST":
        data=request.POST
        print(data["name"])
        return render(request, 'home.html')
