from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    katalog_context = {
        'list_item': data_barang_katalog,
        'nama': 'Rafif Naufal Rahmadika',
        'npm': '2106636275'
    }
    return render(request, "katalog.html", katalog_context)
    