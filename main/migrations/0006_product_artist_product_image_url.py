# Generated by Django 4.2.5 on 2023-09-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='artist',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]