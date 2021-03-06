from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^$', consulta_productores, name='consulta-productores'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^educacion/$', educacion, name='educacion'),
    url(r'^tenencia-propiedad/$', tenencia_propiedad, name='tenencia-propiedad'),
    url(r'^uso-tierra/$', uso_tierra, name='uso-tierra'),
    url(r'^reforestacion/$', reforestacion, name='reforestacion'),
    url(r'^caracterizacion-terreno/$', caracterizacion_terreno, name='caracterizacion-terreno'),
    url(r'^riesgos-finca/$', riesgos_finca, name='riesgos-finca'),
    url(r'^mitigacion-riesgos/$', mitigacion_riesgos, name='mitigacion-riesgos'),
    url(r'^organizacion-productiva/$', organizacion_productiva, name='organizacion-productiva'),
    url(r'^produccion/$', produccion, name='produccion'),
    url(r'^certificacion/$', certificacion, name='certificacion'),
    url(r'^tecnicas-aplicadas/$', tecnicas_aplicadas, name='tecnicas-aplicadas'),
    url(r'^comercializacion/$', comercializacion, name='comercializacion'),
    url(r'^capacitaciones/$', capacitaciones, name='capacitaciones'),
    url(r'^problemas-areas-cacao/$', problemas_areas_cacao, name='problemas-areas-cacao'),
    url(r'^genero/$', genero, name='genero'),
    url(r'^ampliar-areas-cacao/$', ampliar_areas_cacao, name='ampliar-areas-cacao'),

    url(r'^ajax/munis/$', get_munis, name='get-munis'),
    url(r'^ajax/comunies/$', get_comunies, name='get-comunies'),
    url(r'^ajax/organi/$', get_organi, name='get-organi'),
    url(r'^mapa/$', obtener_lista, name='obtener-lista'),
    url(r'^indicadores/$', indicadores, name='indicadores'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
