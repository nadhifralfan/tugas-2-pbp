# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_mywatchlist_html
from mywatchlist.views import show_mywatchlist_xml
from mywatchlist.views import show_mywatchlist_json
from mywatchlist.views import show_mywatchlist_json_by_id
from mywatchlist.views import show_mywatchlist_xml_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('html/', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('xml/', show_mywatchlist_xml, name='show_xml'),
    path('json/', show_mywatchlist_json, name='show_json'),
    path('json/<int:id>', show_mywatchlist_json_by_id, name='show_mywatchlist_json_by_id'),
    path('xml/<int:id>', show_mywatchlist_xml_by_id, name='show_mywatchlist_xml_by_id'),
]