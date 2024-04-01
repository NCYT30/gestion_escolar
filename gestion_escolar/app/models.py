from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    edad = models.IntegerField()
    genero = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    grado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='profesores/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.IntegerField()
    ano_academico = models.IntegerField()
    duracion = models.CharField(max_length=50)
    requisitos_previos = models.TextField()
    materiales_requeridos = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class CalificacionDetalle(models.Model):
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)
    calificacion_valor = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_calificacion = models.DateField()
    tipo_calificacion = models.CharField(max_length=50)

class Horario(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    periodo_academico = models.CharField(max_length=50)

class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo_ausencia = models.CharField(max_length=50)

class Aula(models.Model):
    numero = models.CharField(max_length=10)
    capacidad = models.IntegerField()
    edificio = models.CharField(max_length=50)
    piso = models.IntegerField()
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.numero

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    tipo_evento = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=255)
    organizador = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre


class AsignaturaProfesores(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)