# Generated by Django 3.0.8 on 2020-08-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFinalLP3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nombrecorto', models.CharField(max_length=30)),
                ('fecha_fundacion', models.DateField()),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]
