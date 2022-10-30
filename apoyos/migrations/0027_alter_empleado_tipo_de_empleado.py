# Generated by Django 4.1.2 on 2022-10-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoyos', '0026_empleado_tipo_de_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='tipo_de_empleado',
            field=models.CharField(choices=[('SINDICALIZADO', 'SINDICALIZADO'), ('EVENTUAL', 'EVENTUAL'), ('CONTRATO', 'CONTRATO'), ('OTROS', 'OTROS')], max_length=20),
        ),
    ]