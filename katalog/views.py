from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    return render(request, "katalog.html", context)

context = {
    'item_list' : CatalogItem.objects.all(),
    'nama' : 'Nadhif Rahman Alfan',
    'student_id' : '2106751783',
}