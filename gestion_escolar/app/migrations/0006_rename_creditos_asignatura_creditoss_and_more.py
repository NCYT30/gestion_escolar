# Generated by Django 5.0.3 on 2024-03-28 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_asignatura_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignatura',
            old_name='creditos',
            new_name='creditoss',
        ),
        migrations.RemoveField(
            model_name='asignatura',
            name='profesores',
        ),
    ]