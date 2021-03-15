# Generated by Django 3.1.6 on 2021-03-15 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20210314_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeanDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean_day', models.DateField()),
                ('mean_per_day', models.DecimalField(decimal_places=3, max_digits=10)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.station')),
            ],
            options={
                'verbose_name': 'Moyenne journalière',
                'verbose_name_plural': 'Moyennes journalières',
            },
        ),
        migrations.CreateModel(
            name='MeanWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean_week', models.DateField()),
                ('mean_per_week', models.DecimalField(decimal_places=3, max_digits=10)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.station')),
            ],
            options={
                'verbose_name': 'Moyenne hebdomadaire',
                'verbose_name_plural': 'Moyennes hebdomadaires',
            },
        ),
        migrations.CreateModel(
            name='MeanYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean_year', models.IntegerField()),
                ('mean_per_year', models.DecimalField(decimal_places=3, max_digits=10)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.station')),
            ],
            options={
                'verbose_name': 'Moyenne annuelle',
                'verbose_name_plural': 'Moyennes annuelles',
            },
        ),
        migrations.DeleteModel(
            name='Mean',
        ),
    ]
