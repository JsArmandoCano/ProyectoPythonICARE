# Generated by Django 4.0.4 on 2022-06-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_dominicales_dia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aviso_name', models.CharField(max_length=50)),
                ('aviso_image', models.ImageField(upload_to='photos/fotos')),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
