# Generated by Django 4.1.2 on 2022-10-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoyos', '0020_seccion_remove_localidad_seccion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Seccion',
        ),
        migrations.AddField(
            model_name='localidad',
            name='seccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]