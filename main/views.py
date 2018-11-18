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
    sensor_list = Sensor.objects.all() #recup list of all sensor
    sensor_list_env = [] #init list for the diffrent dict
    # dict form : [{lat:xx.xx, log:xx.xx, data_env: {temeture:xx.x, humidity:xx.x, noise:xx.x}]
    for sensor in sensor_list:
        data ={}
        data['latitude'] = sensor.latitude
        data['longitude'] = sensor.longitude
        data['data_env'] = Log.data_env_latest(sensor.token) # recup the last entry
        #with dat_env_latest function of model.py
        sensor_list_env.append(data) #add the previous data to the list
    return render(request,'main/map.html', locals())

def log_send_by_url(request, uuid, tempeture, humidity, noise):
    """recup env data from the url and save them in the data base"""
    if Sensor.objects.filter(token=uuid).exists():  #see if the uuid is existing
        newLog = Log(id_log=Log.autoid(uuid),token=uuid,tempeture = float(tempeture)/100,
            humidity = float(humidity)/100, noise = int(noise))
    #create new log with: uuid, tempeture/100, humidity/100 and noise (/100 because api format)
        newLog.save() #save the new entry in the database
        return render(request, 'main/home.html',locals())
    else: # if uuid does not exist
         return HttpResponse(status=401)
         #error 401: Unauthorized sensor
