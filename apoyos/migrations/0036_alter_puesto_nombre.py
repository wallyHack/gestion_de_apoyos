# Generated by Django 4.1.3 on 2022-12-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoyos', '0035_alter_empleado_genero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puesto',
            name='nombre',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]