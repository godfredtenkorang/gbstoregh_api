# Generated by Django 5.1.4 on 2024-12-29 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='default.jpg', upload_to='product_img/one'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='default.jpg', upload_to='product_img/two'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='default.jpg', upload_to='product_img/three'),
        ),
    ]
