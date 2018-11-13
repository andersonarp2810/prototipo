from django.shortcuts import render
from .models import Produto, Foto

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    fotos = Foto.objects.all()
    return render(request, 'home_page.html', {'produtos': produtos, 'fotos': fotos})

def produto(request, id):
    produto = Produto.objects.get(pk=id)
    fotos = Foto.objects.filter(produto=produto)
    return render(request,  'product-page.html', {'produto': produto, 'fotos': fotos, 'descontado': produto.preco - produto.desconto})

def pagamento(request):
    return render(request, 'checkout-page.html', {})    