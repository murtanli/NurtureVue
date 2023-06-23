from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import *

@login_required
def profile(request):
    user = request.user.id
    pr = Profile.objects.get(user=user)
    gr = greenhouse.objects.filter(profile=pr)

    registries = []

    for greenhouse2 in gr:
        latest_registry = registry.objects.filter(greenhouse=greenhouse2).latest('datetime')
        registries.append(latest_registry)

    k = gr.count()
    return render(request, 'monitoring/profile.html',context={'registry':registries,'greenhouses': gr,'name':pr,'gr':k})

def update_data(request):
    user = request.user.id
    pr = Profile.objects.get(user=user)
    gr = greenhouse.objects.filter(profile=pr)
    k = gr.count()
    geenhouses = registry.objects.filter(greenhouse__in=gr)
    lit = errors = energy = 0

    for grhs in geenhouses:
        lit += grhs.water
        errors += grhs.error
        energy += grhs.energy
    latest_registry = registry.objects.latest('datetime')
    data = {
        'humidity': k,
        'lit': lit,
        'error': errors,
        'energy': energy,
    }
    return JsonResponse(data)

def map_data(request):
    user = request.user.id
    pr = Profile.objects.get(user=user)
    gr = greenhouse.objects.filter(profile=pr)


    data = {
        'greenhouses': [{'latitude': greenhouse.latitude, 'longitude': greenhouse.longitude} for greenhouse in gr]
    }
    return JsonResponse(data)