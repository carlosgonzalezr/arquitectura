from django.urls import path
from .views import  page_agenda, listar_horas, agenda_medico, pago_atencion, personal


urlpatterns = [

    path('agenda', page_agenda, name="page_agenda"),
    path('lista', listar_horas, name="page_lista"),
    path('agenda-medico', agenda_medico, name="page_agenda_medico"),
    path('pago-atencion', pago_atencion, name="page_pago_atencion"),
    path('personal', personal, name="page_personal")

]