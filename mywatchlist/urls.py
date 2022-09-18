# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_mywatchlist_html
from mywatchlist.views import show_xml
from mywatchlist.views import show_json

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('html/', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]