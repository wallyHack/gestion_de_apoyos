# Generated by Django 4.1.2 on 2022-11-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoyos', '0033_alter_persona_curp'),
    ]

    operations = [
        migrations.AddField(
            model_name='encargadoruta',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images-er'),
        ),
    ]
