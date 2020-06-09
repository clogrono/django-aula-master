"""
    This module contains utility methods to construct the information
    to be downloaded by the descarregues app
""" 

import csv

from django.http import HttpResponse

from aula.apps.alumnes.models import Alumne, Grup
from aula.apps.usuaris.models import Professor
from aula.apps.tutoria.models import Tutor

_OPCIO_TOTS = '-- TOTS --'

def compose_alumnes_csv_response(filtres=None):
    """ composes the alumnes data in a csv format and returns it as a http response
        It accepts filtres as a dict with keys:
            'grups': list of groups names
    """
    def filtra_alumnes(filtres):
        """ retorna els alumnes que respecten els filtres indicats """
        alumnes = Alumne.objects.all()
        tutors = Tutor.objects.all()
        grups = []

        if not filtres:
            return alumnes

        if 'tutors' in filtres:
            if _OPCIO_TOTS not in filtres['tutors']:                
                for t in tutors:
                        if t.professor.last_name in filtres['tutors']:
                            grups.append(t.grup.descripcio_grup)

                alumnes = [a
                    for a in alumnes
                    if a.grup.descripcio_grup in grups ]
        return alumnes

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="alumnes.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nom', 'Cognoms', 'Grup', 'Data de naixement'])

    alumnes = filtra_alumnes(filtres)
    for alumne in alumnes:
        row = [alumne.nom, alumne.cognoms, alumne.grup, alumne.data_neixement]
        writer.writerow(row)

    return response

def  composa_opcions_tutors():
    """ returns a list with the groups as a tuple (display name, group) """
    opcio_tots = [ (_OPCIO_TOTS, _OPCIO_TOTS) ]
    return opcio_tots + [(t.professor.last_name, t.professor.last_name)
                         for t in Tutor.objects.all()]