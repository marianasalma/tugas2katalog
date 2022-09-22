from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_watchlist(request):
    data_watchlist = WatchlistItem.objects.all()
    watched_true = WatchlistItem.objects.filter(watched=True)
    watched_false = WatchlistItem.objects.filter(watched=False)
    context = {
        'list_watchlist': data_watchlist,
        'number_watched' : watched_true.count,
        'number_not_watched' : watched_false.count,
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
