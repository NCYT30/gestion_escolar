# Generated by Django 5.0.3 on 2024-03-28 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_asignaturaprofesores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignatura',
            old_name='creditoss',
            new_name='creditos',
        ),
    ]