# Generated by Django 4.0.4 on 2022-05-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento_name', models.CharField(max_length=50)),
                ('evento_image', models.ImageField(upload_to='photos/fotos')),
                ('description_1', models.CharField(max_length=100)),
                ('description_2', models.CharField(max_length=300)),
                ('fecha_evento', models.DateField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]