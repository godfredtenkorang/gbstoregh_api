# Generated by Django 5.1.4 on 2024-12-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
    ]