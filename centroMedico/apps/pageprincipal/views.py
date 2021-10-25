from django.shortcuts import render
from .forms import AgendaForm

def page_principal(request):
    return render(request, 'pageprincipal/pagina_principal.html', {})

def page_sucursal(request):
    return render(request, 'pageprincipal/sucursales.html', {})    

def page_agenda(request):

    data = {

        'form':AgendaForm()
    }

    if request.method == 'POST':
        formulario = AgendaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Ingreso De Agenda Exitoso"
        else:
            data["form"] = formulario   
    return render(request, 'pageprincipal/agenda.html', data)    
