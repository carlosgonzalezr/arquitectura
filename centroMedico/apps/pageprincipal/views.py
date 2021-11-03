from django.shortcuts import render


def page_principal(request):
    return render(request, 'pageprincipal/pagina_principal.html', {})

def page_sucursal(request):
    return render(request, 'pageprincipal/sucursales.html', {})    
  
