
#https://www.influxdata.com/blog/getting-started-python-influxdb/

from time import sleep
from datetime import *
from influxdb import InfluxDBClient
import numpy as np
import random

#Conectarse a la case de datos
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'Health')
#Crear base de datos
client.create_database('Health')

times = datetime.utcnow();
for i in range(7000000):
    nivelAzucar = round(random.uniform(10,200),2)
    ritmoCardiaco = round(random.uniform(50,210),2)
    calorias = round(random.uniform(0,2000),2)
    times = times + timedelta(minutes = 1)
    sensores = [{'measurement': 'sensor',
                    'tags':{'tipo':'medidorInsulina'},
                    'time':times.isoformat(),
                    'fields': {'nivelAzucar':nivelAzucar}},
                    {'measurement': 'sensor',
                    'tags':{'tipo':'reloj'},
                    'time':times.isoformat(),
                    'fields': {'ritmoCardiaco':ritmoCardiaco}},
                    {'measurement': 'sensor',
                    'tags':{'tipo':'reloj'},
                    'time':times.isoformat(),
                    'fields': {'calorias':ritmoCardiaco}}]
    client.write_points(sensores)

for i in range(7000000):
    caloriasIngeridas = round(random.uniform(10,1000),2)
    caloriasQuemadas = round(random.uniform(0,2000),2)
    times = times + timedelta(minutes = 1)
    calorias = [{'measurement': 'porcentajeCalorico',
                    'tags':{'tipo':'reloj'},
                    'time':times.isoformat(),
                    'fields': {'caloriasIngeridas':caloriasIngeridas}},
                    {'measurement': 'porcentajeCalorico',
                    'tags':{'tipo':'reloj'},
                    'time':times.isoformat(),
                    'fields': {'caloriasQuemadas':caloriasQuemadas}}]
    client.write_points(calorias)

for i in range(7000000):
    pasosTotales = round(random.uniform(0,1000),2)
    times = times + timedelta(minutes = 1)
    pasos = [{'measurement': 'pasos',
                    'tags':{'tipo':'reloj'},
                    'time':times.isoformat(),
                    'fields': {'pasosTotales':pasosTotales}}]
    client.write_points(pasos)
