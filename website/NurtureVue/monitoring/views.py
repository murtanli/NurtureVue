from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import *

@login_required
def profile(request):
    user = request.user.id
    pr = Profile.objects.get(user=user)
    gr = greenhouse.objects.filter(profile=pr)
    k = 0
    for i in gr:
        print(i)
        k=+1

    return render(request, 'monitoring/profile.html',context={'name':pr,'gr':k})