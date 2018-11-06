from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=10)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    cor = models.CharField(max_length=100)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.nome

    
class Foto(models.Model):
    foto = models.ImageField(upload_to='photos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.produto.nome + self.foto.url