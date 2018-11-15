#Views.py of the main app

from django.shortcuts import render
from django.http import HttpResponse
from .models import Log, Sensor


# main function
def home(request):
    """home page request"""
    return render(request, 'main/home.html')

#map function
def map(request):
    """create sensor list and send it to the template"""
    sensor_list = Sensor.objects.all()
    sensor_list_env = []
    # dict : [{lat:xx.xx, log:xx.xx, data_env: {temeture:xx.x, humidity:xx.x, noise:xx.x}]
    for sensor in sensor_list:
        data ={}
        data['latitude'] = sensor.latitude
        data['longitude'] = sensor.longitude
        data['data_env'] = Log.data_env_latest(sensor.token)
        sensor_list_env.append(data)
    return render(request,'main/map.html', locals())

def log_send_by_url(request, uuid, tempeture, humidity, noise):
    """recup env data from the url and save them in the data base"""
    if Sensor.objects.filter(token=uuid).exists():
        existSensor = "sensor is exists" #for test
        newLog = Log(id_log=Log.autoid(uuid),token=uuid,tempeture = float(tempeture)/100,
            humidity = float(humidity)/100, noise = int(noise))
        newLog.save()
        return render(request, 'main/home.html',locals())
    else:
         return HttpResponse(status=401)
