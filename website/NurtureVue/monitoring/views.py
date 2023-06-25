import json
import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
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

            new_registry.save()
            data = {
                'heh': new_registry.id,
            }
        else:
            data = {
                'heh': 'none',
            }
        return JsonResponse(data)

def graphs(request, tepl_id):
    request.session['tepl_id'] = tepl_id
    tepl = greenhouse.objects.get(id=tepl_id)
    post = registry.objects.filter(greenhouse=tepl).latest('datetime')

    data = {
        'id': post.pk,
        'tepl': post.greenhouse,
        'temperature': post.temperature,
        'brightness_of_lights': post.brightness_of_lights,
        'soil_moisture': post.soil_moisture,
        'water2': post.water,
        'energy2': post.energy,
        'error2': post.error,
    }

    return render(request, 'monitoring/graphs.html', context= data)

def graph_view(request):
    tepl_id = request.session.get('tepl_id')
    if tepl_id is not None:
        registries = registry.objects.filter(greenhouse_id=tepl_id)
        data = {
            'temperature': [r.temperature for r in registries],
            'humidity': [r.humidity for r in registries],
            'water': [r.water for r in registries],
            'energy': [r.energy for r in registries],
            'soil_moisture': [r.soil_moisture for r in registries],
            'brightness_of_lights': [r.brightness_of_lights for r in registries],
            'error': [r.error for r in registries],

        }
        return JsonResponse(data)
    else:
        data = {
            'none': 'none'
        }
    return JsonResponse(data)



