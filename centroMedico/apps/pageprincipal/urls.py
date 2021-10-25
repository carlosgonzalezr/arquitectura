from django.urls import path
from .views import page_principal, page_sucursal, page_agenda

urlpatterns = [

    path('', page_principal, name="page_principal"),
    path('sucursales', page_sucursal, name="page_sucursal"),
    path('agenda', page_agenda, name="page_agenda")

]