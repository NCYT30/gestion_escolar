# Generated by Django 5.0.3 on 2024-03-22 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_asignatura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignatura',
            name='cursos',
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesores',
            field=models.ManyToManyField(to='app.profesor'),
        ),
    ]
