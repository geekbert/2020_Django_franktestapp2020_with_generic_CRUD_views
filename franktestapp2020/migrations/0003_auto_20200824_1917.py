# Generated by Django 3.1 on 2020-08-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('franktestapp2020', '0002_yearlydata_year_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearlydata',
            name='people',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlydata',
            name='revenues',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlydata',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlydata',
            name='year_name',
            field=models.CharField(default=models.IntegerField(), max_length=5),
        ),
    ]
