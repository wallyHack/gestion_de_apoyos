# Generated by Django 4.1.2 on 2022-10-13 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apoyos', '0007_alter_apoyos_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='apoyos',
            name='encargado',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='apoyos.encargadoruta'),
            preserve_default=False,
        ),
    ]
