# Generated by Django 4.1 on 2022-08-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pub_field',
        ),
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='project',
            name='product_description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='project',
            name='product_title',
            field=models.CharField(max_length=200, verbose_name='Название продукта'),
        ),
    ]
