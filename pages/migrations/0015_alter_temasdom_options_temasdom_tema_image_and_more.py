# Generated by Django 4.0.4 on 2022-08-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_temasdom_alter_avisos_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temasdom',
            options={'verbose_name': 'Tema', 'verbose_name_plural': 'Temas'},
        ),
        migrations.AddField(
            model_name='temasdom',
            name='tema_image',
            field=models.ImageField(default=None, upload_to='photos/fotos', verbose_name='Imagen:'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre de la Categoria:'),
        ),
    ]
