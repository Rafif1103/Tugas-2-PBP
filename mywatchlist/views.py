from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_film = MyWatchList.objects.all()
    counter = 0
    for film in data_film:
        if(film.is_watched == "Yes"):
            counter+=1
    if(counter < 10 - counter):
        pesan = "Wah, kamu masih sedikit menonton!"
    else:
        pesan = "Selamat, kamu sudah banyak menonton!"
    context = {
        'watchlist': data_film,
        'nama': 'Rafif Naufal Rahmadika',
        'npm': '2106636275',
        'message': pesan
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id (request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id (request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

