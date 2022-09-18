from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.
def show_mywatchlist_html(request):
    return render(request,"mywatchlist.html",context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

data = MyWatchList.objects.all()

context = {
    'watch_list' : data,
    'name' : 'Nadhif Rahman Alfan',
    'student_id' : '2106751783',
}