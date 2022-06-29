# Generated by Django 4.0.3 on 2022-06-29 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacantes', '0004_alter_vacantesmodel_tipo_trabajo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacantesmodel',
            name='tipo_trabajo',
            field=models.CharField(choices=[('Tiempo Completo', 'TIEMPO_COMPLETO'), ('Medio Tiempo', 'MEDIO_TIEMPO'), ('Proyecto', 'PROYECTO')], max_length=30),
        ),
    ]
