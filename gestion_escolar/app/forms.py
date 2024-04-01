from django import forms
from .models import *



class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = '__all__'


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class AsignaturaProfesoresForm(forms.ModelForm):
    class Meta:
        model = AsignaturaProfesores
        fields = ['asignatura', 'profesor']

    def __init__(self, *args, **kwargs):
        super(AsignaturaProfesoresForm, self).__init__(*args, **kwargs)


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['curso', 'profesor', 'dia_semana', 'hora_inicio', 'hora_fin', 'periodo_academico']

    
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estudiante', 'curso']