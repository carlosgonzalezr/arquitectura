from django.shortcuts import render
from .forms import AgendaForm
from .models import Agenda


def page_agenda(request):

    data = {

        'form':AgendaForm()
    }
    #cambiar dato del paciente y agregarle el usuario logeado
    if request.method == 'POST':        
        formulario = AgendaForm(data=request.POST)  
        if formulario.is_valid():
            post = formulario.save(commit=False)
            ##modificar el campo de paciente
            post.paciente = request.user.username
            post.save()
            data["mensaje"] = "Ingreso De Agenda Exitoso"
        else:
            data["form"] = formulario   
    return render(request, 'agenda/agenda.html', data)

def listar_horas(request):
    ## trae todos los registros de la tabla Agenda
    agenda = Agenda.objects.all()
    return render(request, 'agenda/lista_toma_hora.html', {"agenda": agenda})


def agenda_medico(request):
    return render(request, 'agenda/agenda_medico.html') 

def pago_atencion(request):
    return render(request, 'agenda/pago.html')  

def personal(request):
    return render(request, 'agenda/persona.html')             


# recordar falta redireccionar mejor la ruta al guardar un registro ruta lista y crear un boton para devolver al formulario
# darle diseño al formulario
#crear la vista agenda medico y poner el calendario y sus registros.
