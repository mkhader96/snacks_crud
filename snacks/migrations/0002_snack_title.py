# Generated by Django 4.1.3 on 2022-12-05 09:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, help_text='Snack Title', max_length=64),
            preserve_default=False,
        ),
    ]
