# Generated by Django 4.1.3 on 2022-12-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoyos', '0038_alter_localidad_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localidad',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
