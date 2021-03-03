# Generated by Django 3.1.6 on 2021-03-01 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name': 'Donnée pluviométrique', 'verbose_name_plural': 'Données pluviométriques'},
        ),
        migrations.AlterModelOptions(
            name='station',
            options={'verbose_name': 'Station pluviométrique', 'verbose_name_plural': 'Stations pluviométriques'},
        ),
        migrations.AddField(
            model_name='station',
            name='description',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='station',
            name='latiture',
            field=models.DecimalField(decimal_places=10, default=18.971187, max_digits=15),
        ),
        migrations.AddField(
            model_name='station',
            name='longitude',
            field=models.DecimalField(decimal_places=10, default=-72.285215, max_digits=15),
        ),
    ]
