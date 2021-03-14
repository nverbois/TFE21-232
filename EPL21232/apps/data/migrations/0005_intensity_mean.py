# Generated by Django 3.1.6 on 2021-03-10 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20210303_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean_day', models.DateField()),
                ('mean_per_day', models.DecimalField(decimal_places=3, max_digits=10)),
                ('mean_per_week', models.DecimalField(decimal_places=3, max_digits=10)),
                ('mean_per_year', models.DecimalField(decimal_places=3, max_digits=10)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.station')),
            ],
            options={
                'verbose_name': 'Moyenne pluviométrique',
                'verbose_name_plural': 'Moyennes pluviométriques',
            },
        ),
        migrations.CreateModel(
            name='Intensity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity_day', models.DateField()),
                ('duration', models.TimeField()),
                ('max_amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('start_interval', models.DecimalField(decimal_places=3, max_digits=10)),
                ('end_interval', models.DecimalField(decimal_places=3, max_digits=10)),
                ('intensity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.station')),
            ],
            options={
                'verbose_name': 'Intensité pluviométrique',
                'verbose_name_plural': 'Intensités pluviométriques',
            },
        ),
    ]