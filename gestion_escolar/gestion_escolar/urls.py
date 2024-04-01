"""
URL configuration for gestion_escolar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login, name = 'login'),
    path('aula/', views.aula, name = 'aula'),
    path('aula/create/', views.aula_create, name='aula_create'),
    path('aula/obtener_datos_aula/<int:aula_id>/', views.obtener_datos_aula, name='obtener_datos_aula'),
    path('aula/update/<int:id>/', views.aula_update, name='aula_update'),
    path('aula/delete/<int:id>/', views.aula_delete, name='aula_delete'),
    path('evento/', views.evento, name = 'evento'),
    path('evento/create/', views.evento_create, name='evento_create'),
    path('evento/obtener_datos_evento/<int:evento_id>/', views.obtener_datos_evento, name='obtener_datos_evento'),
    path('evento/update/<int:id>/', views.evento_update, name='evento_update'),
    path('evento/delete/<int:id>/', views.evento_delete, name='evento_delete'),
    path('asignatura/', views.asignatura, name = 'asignatura'),
    path('asignatura/create/', views.asignatura_create, name = 'asignatura_create'),
    path('asignatura/obtener_datos_asignatura/<int:asignatura_id>/', views.obtener_datos_asignatura, name='obtener_datos_asignatura'),
    path('asignatura/update/<int:id>/', views.asignatura_update, name = 'asignatura_update'),
    path('asignatura/delete/<int:id>/', views.asignatura_delete, name='asignatura_delete'),
    path('profesor/', views.profesor, name='profesor'),
    path('profesor/create/', views.profesor_create, name='profesor_create'),
    path('profesor/update/<int:pk>/', views.profesor_update, name='profesor_update'),
    path('profesor/delete/<int:pk>/', views.profesor_delete, name='profesor_delete'),
    path('asigprofe/', views.asignaturas_profesores, name='asigprofe'),
    path('asigprofe/create/', views.asignatura_profesor_create, name='asignatura_profesor_create'),
    path('asigprofe/obtener_datos_asigprofe/<int:asigprofe_id>/', views.obtener_datos_asigprofe, name='obtener_datos_asigprofe'),
    path('asigprofe/update/<int:id>/', views.asignatura_profesor_update, name='asignatura_profesor_update'),
    path('asigprofe/delete/<int:id>/', views.asignatura_profesor_delete, name='asignatura_profesor_delete'),
    path('curso/', views.curso, name='curso'),
    path('curso/create/', views.curso_create, name='curso_create'),
    path('curso/obtener_datos_curso/<int:curso_id>/', views.obtener_datos_curso, name='obtener_datos_curso'),
    path('curso/update/<int:pk>/', views.curso_update, name='curso_update'),
    path('curso/delete/<int:pk>/', views.curso_delete, name='curso_delete'),
    path('horario/', views.horario, name='horario'),
    path('horario/create/', views.horario_create, name='horario_create'),
    path('horario/obtener_datos_horario/<int:horario_id>/', views.obtener_datos_horario, name='obtener_datos_horario'),
    path('horario/update/<int:pk>/', views.horario_update, name='horario_update'),
    path('horario/delete/<int:pk>/', views.horario_delete, name='horario_delete'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiantes/create/', views.estudiantes_create, name='estudiantes_create'),
    path('estudiantes/obtener_datos_estudiante/<int:estudiante_id>/', views.obtener_datos_estudiante, name='obtener_datos_estudiante'),
    path('estudiantes/update/<int:pk>/', views.estudiantes_update, name='estudiantes_update'),
    path('estudiantes/delete/<int:pk>/', views.estudiantes_delete, name='estudiantes_delete'),
    path('calificaciones/', views.calificaciones, name='calificaciones'),
    path('calificaciones/create/', views.calificacion_create, name='calificacion_create'),
    path('calificaciones/obtener_datos_calificacion/<int:calificaciones_id>/', views.obtener_datos_calificacion, name='obtener_datos_calificacion'),
    path('calificaciones/update/<int:pk>/', views.calificacion_update, name='calificacion_update'),
    path('calificaciones/delete/<int:pk>/', views.calificacion_delete, name='calificacion_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)