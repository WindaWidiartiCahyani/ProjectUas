from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from widiarti.models import Produk
from .keranjang import Cahyani
from .forms import CahyaniAddProductForm


@require_POST
def cahyani_add(request, product_id):
    cahyani = Cahyani(request) # create a new cart object passing it the request object 
    product = get_object_or_404(Produk, id=product_id) 
    quantity = int(request.POST.get('quantity'))
    form = CahyaniAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cahyani.add(product=product, quantity=quantity, update_quantity=cd['update'])
    return redirect('cahyani_detail')

def cahyani_remove(request, product_id):
    cahyani = Cahyani(request)
    product = get_object_or_404(Produk, id=product_id)
    cahyani.remove(product)
    return redirect('cahyani_detail')

def cahyani_detail(request):
    cahyani = Cahyani(request)
    context = {
            'judul': 'Halaman Pemesanan Produk',
            'cahyani':cahyani
        }
    for item in cahyani:
        item['update_quantity_form'] = CahyaniAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'pemesanan.html',context)

