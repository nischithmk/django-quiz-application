# Generated by Django 4.1.2 on 2022-10-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_create_initial_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
