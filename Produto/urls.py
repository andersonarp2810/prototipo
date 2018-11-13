from django.urls import path
from .views import index, produto

urlpatterns = [
    path('home', index, name="home"),
    path('produto/<int:id>', produto, name="produto_show"),
]