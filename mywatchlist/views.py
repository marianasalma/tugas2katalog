from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_watchlist(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
        'list_watchlist': data_watchlist,
        'nama': 'Mariana Salma',
        'npm' : '2106702516'
    }
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
