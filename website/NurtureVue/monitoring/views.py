import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.datetime_safe import datetime
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import CreateView

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
    return render(request, 'monitoring/profile.html', context={'registry': registries, 'greenhouses': gr, 'name': pr, 'gr': k})


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

def test(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    gr = greenhouse.objects.filter(profile=profile)
    context = {
        'gr':gr
    }
    return render(request, 'monitoring/test.html',context= context)

class save_db(View, LoginRequiredMixin):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            profile = Profile.objects.get(user=user)
            gr = greenhouse.objects.filter(profile=profile)
            num = gr.latest('id')
            new_registry = registry()


            new_registry.greenhouse = num
            new_registry.datetime = datetime.now()
            new_registry.humidity = random.randint(0, 100)
            new_registry.water = random.randint(0, 1000)
            new_registry.temperature = random.randint(0, 40)
            new_registry.energy = random.randint(0, 1000)
            new_registry.soil_moisture = random.randint(0, 100)
            new_registry.brightness_of_lights = random.randint(0, 100)
            new_registry.heating = random.randint(0, 1)
            new_registry.ventilation = random.randint(0, 1)
            new_registry.window1 = random.randint(0, 1)
            new_registry.window2 = random.randint(0, 1)
            new_registry.pump1 = random.randint(0, 1)
            new_registry.pump2 = random.randint(0, 1)
            new_registry.error = random.randint(0, 10)
            # не работает нужно пербразовать в json

            new_registry.save()
            data = {
                'heh': new_registry.id,
                'greenhouse': new_registry.greenhouse,

            }
        else:
            data = {
                'heh': 'none',
            }
        return JsonResponse(data)


