# Generated by Django 3.2.5 on 2021-12-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='case',
            fields=[
                ('ID', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='case_id')),
                ('gender', models.CharField(max_length=10, verbose_name='gerder')),
                ('stage', models.CharField(max_length=5, verbose_name='tumor_stage')),
                ('age', models.IntegerField(default='', verbose_name='age')),
                ('height', models.FloatField(default='', verbose_name='height_cm')),
                ('weight', models.FloatField(default='', verbose_name='weight_kg')),
            ],
        ),
    ]
