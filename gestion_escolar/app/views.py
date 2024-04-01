from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import os
from django.conf import settings


def base(request):
    asignaturas_disponibles = Asignatura.objects.all()
    profesores_disponibles = Profesor.objects.all()
    return render(request, 'base.html', {'asignaturas_disponibles': asignaturas_disponibles, 'profesores_disponibles': profesores_disponibles})


def login(request):
    return render(request, 'login.html')

def aula(request):
    aulas = Aula.objects.all()
    return render(request, 'aula.html', {'aulas': aulas}) 

from django.http import JsonResponse

def obtener_datos_aula(request, aula_id):
    try:
        aula = Aula.objects.get(id=aula_id)

        data = {
            'numero': aula.numero,
            'capacidad': aula.capacidad,
            'edificio': aula.edificio,
            'piso': aula.piso,
            'ubicacion': aula.ubicacion
        }
        return JsonResponse(data)
    except Aula.DoesNotExist:
        return JsonResponse({'error': 'Aula no encontrada'}, status=404)
    except Exception as e:
        print('Error en obtener_datos_aula:', e)
        return JsonResponse({'error': 'Error interno del servidor'}, status=500)


def aula_detail(request, id):
    aula = get_object_or_404(Aula, id=id)
    return render(request, 'aula_detail.html', {'aula': aula})

def aula_create(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aula')
    else:
        form = AulaForm()
    return render(request, 'aula.html', {'form': form})



def aula_update(request, id):
    try:
        aula = get_object_or_404(Aula, id=id)
        if request.method == 'POST':
            form = AulaForm(request.POST, instance=aula)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Aula actualizada con éxito'})
        else:
            form = AulaForm(instance=aula)
        return JsonResponse({'error': 'Error al actualizar el aula'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def aula_delete(request, id):
    aula = get_object_or_404(Aula, id=id)
    if request.method == 'POST':
        aula.delete()
        return redirect('aula')
    return render(request, 'aula.html', {'aula': aula})


def evento(request):
    evento = Evento.objects.all()
    return render(request, 'evento.html', {'evento': evento})



def obtener_datos_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    data = {
        'nombre': evento.nombre,
        'descripcion': evento.descripcion,
        'fecha': evento.fecha,
        'tipo_evento': evento.tipo_evento,
        'ubicacion': evento.ubicacion,
        'organizador': evento.organizador
    }
    return JsonResponse(data)


def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento')
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = EventoForm()
    return render(request, 'evento.html', {'form': form})



def evento_update(request, id):
    try:
        evento = get_object_or_404(Evento, id=id)
        if request.method == 'POST':
            form = EventoForm(request.POST, instance=evento)
            if form.is_valid():
                form.save()
                return redirect('evento')
            else:
                return JsonResponse({'error': 'Error al actualizar el evento'}, status=500)
        else:
            form = EventoForm(instance=evento)
        return render(request, 'evento.html', {'form': form, 'evento_id': id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def evento_delete(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento')
    return render(request, 'evento.html', {'evento': evento})


def asignatura(request):
    asignatura = Asignatura.objects.all()
    return render(request, 'asignatura.html', {'asignatura': asignatura})


def asignatura_create(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asignatura')
    else:
        form = AsignaturaForm()
    
    errors = {}
    for field, field_errors in form.errors.items():
        errors[field] = field_errors[0]
    
    return JsonResponse({'errors': errors}, status=400)


def obtener_datos_asignatura(request, asignatura_id):
    asignatura = Asignatura.objects.get(id=asignatura_id)
    data = {
        'nombre': asignatura.nombre,
        'descripcion': asignatura.descripcion,
        'creditos': asignatura.creditos
    }
    return JsonResponse(data)


def asignatura_update(request, id):
    try:
        asignatura = get_object_or_404(Asignatura, id=id)
        if request.method == 'POST':
            form = AsignaturaForm(request.POST, instance=asignatura)
            if form.is_valid():
                form.save()
                return redirect('asignatura')
            else:
                return JsonResponse({'error': 'Error al actualizar la asignatura'}, status=500)
        else:
            form = EventoForm(instance=asignatura)
        return render(request, 'asignatura.html', {'form': form, 'asignatura_id': id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def asignatura_delete(request, id):
    asignatura = get_object_or_404(Asignatura, id=id)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('asignatura')
    return render(request, 'asignatura.html', {'asignatura': asignatura})


def profesor(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor.html', {'profesores': profesores})


def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['foto']
            file_name = os.path.join('profesores', image_file.name)
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)


            with open(file_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            form.instance.foto = file_name

            form.save()
            return redirect('profesor')
    else:
        form = ProfesorForm()
    return render(request, 'profesor.html', {'form': form})



def profesor_update(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, request.FILES, instance=profesor)
        if form.is_valid():

            if 'foto' in request.FILES:
                if profesor.foto:
                    file_path = os.path.join(settings.MEDIA_ROOT, profesor.foto.name)
                    if os.path.exists(file_path):
                        os.remove(file_path)

                image_file = request.FILES['foto']
                file_name = os.path.join('profesores', image_file.name)
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)

                with open(file_path, 'wb+') as destination:
                    for chunk in image_file.chunks():
                        destination.write(chunk)

                form.instance.foto = file_name

            form.save()
            return redirect('profesor')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'profesor.html', {'form': form, 'profesor': profesor})


def profesor_delete(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('profesor')
    return render(request, 'profesor.html', {'profesor': profesor})




def asignaturas_profesores(request):
    asignaturas_disponibles = Asignatura.objects.all()
    profesores_disponibles = Profesor.objects.all()
    asignaturas_profesores = AsignaturaProfesores.objects.all()
    return render(request, 'asigprofe.html', {'asignaturas_profesores': asignaturas_profesores, 'asignaturas_disponibles': asignaturas_disponibles, 'profesores_disponibles': profesores_disponibles})



def asignatura_profesor_create(request):
    if request.method == 'POST':
        form = AsignaturaProfesoresForm(request.POST)
        if form.is_valid():
            asignatura_profesor = form.save()
            return redirect('asigprofe')
    else:
        form = AsignaturaProfesoresForm()
    return render(request, 'asigprofe.html', {'form': form})


def obtener_datos_asigprofe(request, asigprofe_id):
    asignatura = Asignatura.objects.get(id=asigprofe_id)
    data = {
        'asignatura': asignatura.nombre,
        'profesor': asignatura.descripcion
    }
    return JsonResponse(data)


def asignatura_profesor_update(request, id):
    asignatura_profesor = AsignaturaProfesores.objects.get(id=id)
    form = AsignaturaProfesoresForm(request.POST or None, instance=asignatura_profesor)
    if form.is_valid():
        form.save()
        return redirect('asigprofe')
    return render(request, 'asigprofe.html', {'form': form})


def asignatura_profesor_delete(request, id):
    asignatura_profesor = AsignaturaProfesores.objects.get(id=id)
    asignatura_profesor.delete()
    return redirect('asigprofe')



def curso(request):
    cursos = Curso.objects.all()
    return render(request, 'curso.html', {'cursos': cursos})


def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso')
    else:
        form = CursoForm()
    return render(request, 'curso.html', {'form': form})


def obtener_datos_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    data = {
        'nombre': curso.nombre,
        'descripcion': curso.descripcion,
        'creditos': curso.creditos,
        'ano_academico': curso.ano_academico,
        'duracion': curso.duracion,
        'requisitos_previos': curso.requisitos_previos,
        'materiales_requeridos': curso.materiales_requeridos,
        'costo': str(curso.costo),
        'estado': curso.estado,
    }
    return JsonResponse(data)


def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso.html', {'form': form})


def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso_list')
    return render(request, 'curso.html', {'curso': curso})


def horario(request):
    cursos_disponibles = Curso.objects.all()
    profesores_disponibles = Profesor.objects.all()
    horarios = Horario.objects.all()
    return render(request, 'horario.html', {
        'cursos_disponibles': cursos_disponibles,
        'profesores_disponibles': profesores_disponibles,
        'horarios': horarios,
    })

def horario_create(request):
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horario')
    else:
        form = HorarioForm()
    return render(request, 'horario.html', {'form': form})


def obtener_datos_horario(request, horario_id):
    horario = Horario.objects.get(id=horario_id)
    data = {
        'curso': horario.curso.nombre,
        'profesor': horario.profesor.nombre,
        'dia_semana': horario.dia_semana,
        'hora_inicio': horario.hora_inicio.strftime('%H:%M:%S'),
        'hora_fin': horario.hora_fin.strftime('%H:%M:%S'),
        'periodo_academico': horario.periodo_academico,
    }
    return JsonResponse(data)


def horario_update(request, pk):
    horario = get_object_or_404(Horario, pk=pk)
    if request.method == 'POST':
        form = HorarioForm(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            return redirect('horario')
    else:
        form = HorarioForm(instance=horario)
    return render(request, 'horario.html', {'form': form})


def horario_delete(request, pk):
    horario = get_object_or_404(Horario, pk=pk)
    if request.method == 'POST':
        horario.delete()
        return redirect('horario')
    return render(request, 'horario.html', {'horario': horario})


def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})


def estudiantes_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'estudiantes.html', {'form': form})


def obtener_datos_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    data = {
        'nombre': estudiante.nombre,
        'fecha_nacimiento': estudiante.fecha_nacimiento.strftime('%Y-%m-%d'),
        'direccion': estudiante.direccion,
        'edad': estudiante.edad,
        'genero': estudiante.genero,
        'email': estudiante.email,
        'telefono': estudiante.telefono,
        'fecha_ingreso': estudiante.fecha_ingreso.strftime('%Y-%m-%d'),
        'grado': estudiante.grado,
    }
    return JsonResponse(data)

def estudiantes_update(request, pk):
    estudiante = Estudiante.objects.get(pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiantes.html', {'form': form})


def estudiantes_delete(request, pk):
    estudiante = Estudiante.objects.get(pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('estudiantes')
    return render(request, 'estudiantes.html', {'estudiante': estudiante})


def calificaciones(request):
    calificaciones = Calificacion.objects.all()
    estudiantes = Estudiante.objects.all()
    cursos = Curso.objects.all()
    return render(request, 'calificaciones.html', {'calificaciones': calificaciones, 'estudiantes': estudiantes, 'cursos': cursos})


def calificacion_create(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'calificaciones.html', {'form': form})


def obtener_datos_calificacion(request, calificacion_id):
    calificacion = Calificacion.objects.get(id=calificacion_id)
    data = {
        'estudiante': calificacion.estudiante.nombre,
        'curso': calificacion.curso.nombre,
    }
    return JsonResponse(data)

def calificacion_update(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificaciones.html', {'form': form})


def calificacion_delete(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('calificaciones')
    return render(request, 'calificaciones.html', {'calificacion': calificacion})