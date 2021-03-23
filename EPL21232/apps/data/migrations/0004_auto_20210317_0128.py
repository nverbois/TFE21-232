# Generated by Django 3.1.6 on 2021-03-17 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20210316_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='valuetest',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='meanday',
            name='data',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='data.data'),
        ),
        migrations.AlterField(
            model_name='meanday',
            name='mean_per_day',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='meanweek',
            name='mean_per_week',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
