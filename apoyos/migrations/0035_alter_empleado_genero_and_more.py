# Generated by Django 4.1.2 on 2022-11-12 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoyos', '0034_encargadoruta_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='genero',
            field=models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], default='Tipo de empleado..', max_length=15),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='tipo_de_empleado',
            field=models.CharField(choices=[('Tipo de empleado..', 'Tipo de empleado..'), ('SINDICALIZADO', 'SINDICALIZADO'), ('EVENTUAL', 'EVENTUAL'), ('CONTRATO', 'CONTRATO'), ('OTROS', 'OTROS')], default='Tipo de empleado..', max_length=20),
        ),
    ]
