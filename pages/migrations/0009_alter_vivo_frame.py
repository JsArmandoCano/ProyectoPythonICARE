# Generated by Django 4.0.4 on 2022-06-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_vivo_frame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivo',
            name='frame',
            field=models.URLField(),
        ),
    ]
