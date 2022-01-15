# Generated by Django 3.2.5 on 2021-12-19 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='variation_order')),
                ('gene', models.CharField(max_length=20, verbose_name='gene_name')),
                ('sd', models.FloatField(verbose_name='standard_deviation')),
            ],
        ),
        migrations.CreateModel(
            name='transtriptome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrg', models.CharField(max_length=20, verbose_name='most-reads-genes')),
                ('count', models.FloatField(verbose_name='most-reads-genes-counts')),
                ('allEx', models.FloatField(verbose_name='total_expression')),
                ('Case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.case')),
            ],
        ),
    ]