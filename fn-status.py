import requests
import tweepy
import time
import os
from os import environ

auth = tweepy.OAuthHandler("wZdsf58Ka2jciAifsd5NDg2y1", "FwbZcX6g9vGbpwLyNejLIHdY9KybOhUdEBHVTvXn6YQpa1MpRY")
auth.set_access_token("1285954782545563649-onwph67OZ10ulwjVO8r7p3CIgSFMnD", "tWeoFkLdvv8qZsYBE4wrooaLpFh331Dalj3AT5S9LtGTY")
api = tweepy.API(auth)

url = 'https://lightswitch-public-service-prod06.ol.epicgames.com/lightswitch/api/service/bulk/status?serviceId=Fortnite'

setDelay = 30

res = requests.get(url).json()
status = res[0]['status']

while 1:
    res = requests.get(url).json()
    statusNew = res[0]['status']

    if status != statusNew:
        try:
            print('El estado del servidor se ha actualizado...')
            if statusNew == 'UP':
                api.update_with_media('assets/status.jpg', '¡El servidor de Fortnite está en línea!')
                print('Publicado correctamente en Twitter. (Online)')
            else:
                api.update_with_media('assets/status.jpg', '¡El servidor de Fortnite no está en línea!')
                print('Publicado correctamente en Twitter. (Offline)')
            status = res[0]['status']
        except:
            print('Error. (1)')
    else:
        print('No se detectan cambios. Buscando de nuevo en 60 segundos...')

    time.sleep(setDelay)




    
