# Generated by Django 4.1.2 on 2022-10-29 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoyos', '0025_alter_apoyos_notas_adicionales'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='tipo_de_empleado',
            field=models.CharField(choices=[('SINDICALIZADO', 'SINDICALIZADO'), ('EVENTUAL', 'EVENTUAL'), ('CONTRATO', 'CONTRATO'), ('OTROS', 'OTROS')], default='SINDICALIZADO', max_length=20),
        ),
    ]
