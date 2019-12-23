from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect

from .forms import SpotForm, BicycleForm
from .models import Spot, Bicycle

from decouple import config
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import requests


def testmapgoogle(request):
    tour_spots = Spot.objects.all()
    tourstr = serializers.serialize("json", tour_spots, cls=DjangoJSONEncoder)
    bike_locations = Bicycle.objects.all()
    # 실시간 대신 여기에서 처리해주는 것으로 하자.
    url = 'http://openapi.seoul.go.kr:8088/' + config("SEOULBIKEKEY") 
    dataurl1 = '/json/bikeList/1/1000/'
    dataurl2 = '/json/bikeList/1001/2000/'
    res = requests.get(url+dataurl1)
    temp = res.json().get('rentBikeStatus').get('row')
    for t in temp:
        possibleBike = t.get('parkingBikeTotCnt')
        stationName = t.get('stationName')
        stationId = stationName.split('.')[0]
        bikeLoc = bike_locations.get(idnum=stationId)
        bikeLoc.possiblebikenum = possibleBike
        bikeLoc.save()
                
    res = requests.get(url+dataurl2)
    temp = res.json().get('rentBikeStatus').get('row')
    for t in temp:
        possibleBike = t.get('parkingBikeTotCnt')
        stationName = t.get('stationName')
        stationId = stationName.split('.')[0]
        bikeLoc = bike_locations.get(idnum=stationId)
        bikeLoc.possiblebikenum = possibleBike
        bikeLoc.save()
    
    bikestr = serializers.serialize("json", bike_locations, cls=DjangoJSONEncoder)
    ctx = {
        'spots': tourstr,
        'bikelocations': bikestr, 
        'tkey': config("TMAPKEY"),
        'googlekey': config("GOOGLEMAPKEY"),
        'seoulbikekey': config("SEOULBIKEKEY"),
    }
    return render(request, 'bike/tempgoogle.html', ctx)

def searchgoogle(request):
    tour_spots = Spot.objects.all()
    tourstr = serializers.serialize("json", tour_spots, cls=DjangoJSONEncoder)
    ctx = {
        "spots": tourstr,
        "googlekey": config("GOOGLEMAPKEY"),
        "seoulbikekey":config("SEOULBIKEKEY"),
    }
    return render(request, 'bike/searchgoogle.html', ctx)




