# Generated by Django 4.1.2 on 2022-11-04 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoyos', '0032_persona_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='curp',
            field=models.CharField(blank=True, max_length=18, null=True, unique=True),
        ),
    ]
