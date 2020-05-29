from django.conf.urls import url
from aula.apps.relacioFamilies import views as relacioFamilies_views

urlpatterns = [
    url(r'^elMeuInforme/$', relacioFamilies_views.elMeuInforme,
        name='relacio_families__informe__el_meu_informe'),
                       
    url(r'^dadesRelacioFamilies/$', relacioFamilies_views.dadesRelacioFamilies,
        name="tutoria__relacio_families__dades_relacio_families"),
    
    url(r'^configuraConnexio/(?P<pk>\d+)/$', relacioFamilies_views.configuraConnexio,
        name="tutoria__relacio_families___configura_connexio"), 
      
    url(r'^bloquejaDesbloqueja/(?P<pk>\d+)/$', relacioFamilies_views.bloquejaDesbloqueja,
        name="tutoria__relacio_families__bloqueja_desbloqueja"), 
      
    url(r'^enviaBenvinguda/(?P<pk>\d+)/$', relacioFamilies_views.enviaBenvinguda,
        name="tutoria__relacio_families__envia_benvinguda"),
    
    url(r'^elMeuInforme/(?P<pk>\d+)/$', relacioFamilies_views.elMeuInforme,
        name="relacio_families__informe__el_meu_informe"),
    
    url(r'^canviParametres/$', relacioFamilies_views.canviParametres,
        name="relacio_families__configuracio__canvi_parametres"),         
]