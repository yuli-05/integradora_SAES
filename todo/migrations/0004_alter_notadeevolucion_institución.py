# Generated by Django 4.0.3 on 2022-04-03 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_notadeevolucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notadeevolucion',
            name='Institución',
            field=models.CharField(max_length=100),
        ),
    ]
