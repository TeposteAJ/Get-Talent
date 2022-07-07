# Generated by Django 4.0.3 on 2022-07-07 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VacantesModel',
            fields=[
                ('vacante_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('descripcion', models.TextField(max_length=500)),
                ('requisitos', models.TextField(max_length=300)),
                ('localidad', models.CharField(default='No aplica', max_length=30)),
                ('sueldo', models.DecimalField(decimal_places=2, default='0.0', max_digits=30)),
                ('tipo_trabajo', models.CharField(choices=[('Tiempo Completo', 'COMPLETO'), ('Medio Tiempo', 'MEDIO'), ('Proyecto', 'PROYECTO'), ('Sin especificar', 'SIN_ESPECIFICAR')], max_length=30)),
                ('modalidad', models.CharField(choices=[('Presencial', 'PRESENCIAL'), ('Virtual', 'VIRTUAL'), ('Hibrido', 'HIBRIDO'), ('Sin especificar', 'SIN_ESPECIFICAR')], max_length=20)),
                ('estado', models.CharField(choices=[('Aguascalientes', 'AGUASCALIENTES'), ('Baja California', 'BAJA_CALIFORNIA'), ('Baja California Sur', 'BAJA_CALIFORNIA_SUR'), ('Campeche', 'CAMPECHE'), ('Chiapas', 'CHIAPAS'), ('Chihuahua', 'CHIHUAHUA'), ('Ciudad de México', 'CD_MEX'), ('Coahuila', 'COAHUILA'), ('Colima', 'COLIMA'), ('Durango', 'DURANGO'), ('Guanajuato', 'GUANAJUATO'), ('Guerrero', 'GUERRERO'), ('Hidalgo', 'HIDALGO'), ('Jalisco', 'JALISCO'), ('Estado de México', 'EDO_MEX'), ('Michoacán', 'MICHOACAN'), ('Morelos', 'MORELOS'), ('Nayarit', 'NAYARIT'), ('Nuevo León', 'NUEVO_LEON'), ('Oaxaca', 'OAXACA'), ('Puebla', 'PUEBLA'), ('Querétaro', 'QUERETARO'), ('Quintana Roo', 'QUINTANA_ROO'), ('San Luis Potosí', 'SAN_LUIS_POTOSI'), ('Sinaloa', 'SINALOA'), ('Sonora', 'SONORA'), ('Tabasco', 'TABASCO'), ('Tamaulipas', 'TAMAULIPAS'), ('Tlaxcala', 'TLAXCALA'), ('Veracruz', 'VERACRUZ'), ('Yucatán', 'YUCATAN'), ('Zacatecas', 'ZACATECAS')], max_length=25)),
                ('area', models.CharField(choices=[('Marketing', 'Marketing'), ('Ventas', 'Ventas'), ('Humanidades', 'Humanidades'), ('Administración', 'Administración'), ('Industria', 'Industria'), ('Analisis de Datos', 'Analista de Datos'), ('Tecnología', 'Tecnología'), ('Desarrollo de Software', 'Desarrollo de Software'), ('Ciencias Exactas', 'Ciencias Exactas')], max_length=60)),
                ('experiencia', models.CharField(choices=[('Becario', 'Inexperto'), ('Primer Empleo', 'Sin experiencia Laboral'), ('Poca Experiencia', 'Poca'), ('Experiencia Media', 'Medio'), ('Mucha experiencia', 'Alto'), ('Cargos ejecutivos', 'Superior')], max_length=60)),
                ('vacante_video', models.CharField(blank=True, max_length=150)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='PreguntasModel',
            fields=[
                ('preguntas_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('pregunta1', models.CharField(max_length=150)),
                ('pregunta2', models.CharField(max_length=150)),
                ('pregunta3', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('vacante_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacantes.vacantesmodel')),
            ],
        ),
    ]
