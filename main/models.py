#models for the main app
from django.db import models
import datetime
import uuid

class Sensor(models.Model):
    """Sensor models"""
    token =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    add_date = models.DateTimeField(auto_now_add=True)
    longitude = models.FloatField() #xx.xx
    latitude = models.FloatField() #xx.xx
    altitude = models.FloatField()

class Log(models.Model):
    """Sensor log"""
    token = models.UUIDField()
    id_log = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tempeture = models.FloatField() #in °c
    humidity = models.FloatField() # in %
    noise = models.FloatField() # in dB

    def autoid(uuid):
        """create a automatic unique id for the log"""
        date = datetime.datetime.now() #recup actual date and hours
        date_str = str(date)
        id_auto = str(uuid) + date_str
        return id_auto


    def data_dict(uuid):
        """create a dict with environmental data """
        env_data = Log.objects.filter(token = uuid) #extract data form the database
        data_dict = {'uuid':uuid}  # dict return by the function
        data_list = []
        for log in temp_data:
            data = {}
            data['tempeture'] = log.tempeture
            data['humidity'] = log.humidity
            data['noise'] = log.noise
            data['date'] = log.date
            data_list.append(data)
        data_dict['log'] = data_list
        return data_dict

    def data_env_latest(uuid):
        """return the latest environmental data"""
        env_data = Log.objects.filter(token = uuid).latest('date') #recup the latest entry
        data = {}
        data['tempeture'] = env_data.tempeture
        data['humidity'] = env_data.humidity
        data['noise'] = env_data.noise
        return data
