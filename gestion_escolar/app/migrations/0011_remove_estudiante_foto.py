# Generated by Django 5.0.3 on 2024-04-01 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_profesor_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='foto',
        ),
    ]