# Generated by Django 4.0.4 on 2022-05-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centraal', '0004_food_f_total_fat_portion_p_total_fat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='f_total_fat',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
