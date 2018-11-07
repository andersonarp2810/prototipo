from django.shortcuts import render
from .models import Produto, Foto

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    fotos = Foto.objects.all()
    return render(request, 'index.html', {'produtos': produtos, 'fotos': fotos})