# Generated by Django 4.1.3 on 2022-12-05 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_snack_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snack',
            name='title',
        ),
        migrations.AddField(
            model_name='snack',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, help_text='Snack Name', max_length=64),
            preserve_default=False,
        ),
    ]
