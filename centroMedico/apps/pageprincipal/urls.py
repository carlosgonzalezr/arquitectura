from django.urls import path
from .views import page_principal, page_sucursal

urlpatterns = [

    path('', page_principal, name="page_principal"),
    path('sucursales', page_sucursal, name="page_sucursal"),

]