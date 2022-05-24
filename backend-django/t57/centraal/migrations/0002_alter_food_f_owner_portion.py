# Generated by Django 4.0.4 on 2022-05-24 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('centraal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='f_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_foods', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Portion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_dry_weight', models.FloatField(blank=True, default=0, null=True)),
                ('p_date', models.DateTimeField(blank=True, null=True)),
                ('p_food', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_portions', to='centraal.food')),
                ('p_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_portions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]