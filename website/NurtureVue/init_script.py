import random
from datetime import datetime
from main.models import *
def populate_database(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    gr = greenhouse.objects.filter(profile=profile)
    num = gr.latest('id')
    print(num)
    new_registry = registry()

    # Присвойте значения полям объекта
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


