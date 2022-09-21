from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.
data = MyWatchList.objects.all()

def show_mywatchlist_html(request):

    context = {
    'watch_list' : data,
    'name' : 'Nadhif Rahman Alfan',
    'student_id' : '2106751783',
    'message' : show_message()
    }

    return render(request,"mywatchlist.html",context)

def show_mywatchlist_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_mywatchlist_json_by_id(request,id):
    data_filter = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_filter), content_type="application/json")

def show_mywatchlist_xml_by_id(request,id):
    data_filter = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_filter), content_type="application/xml")

def show_message():
    done = 0
    undone = 0
    for watchlist in data:
        if watchlist.watched:
            done += 1
        else:
            undone += 1
    if done >= undone:
        return "Selamat, kamu sudah banyak menonton!"
    return "Wah, kamu masih sedikit menonton!"