# Generated by Django 4.1.3 on 2022-12-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoyos', '0037_alter_departamento_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localidad',
            name='nombre',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
