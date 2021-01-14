# Generated by Django 3.1.5 on 2021-01-14 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20210109_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='rolepriority',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamMember', to='teams.team'),
        ),
    ]
