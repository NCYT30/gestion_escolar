# Generated by Django 5.0.3 on 2024-03-28 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_creditos_asignatura_creditoss_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignaturaProfesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.asignatura')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profesor')),
            ],
        ),
    ]