# Generated by Django 3.2.6 on 2023-05-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.FileField(null=True, upload_to='products/videos/'),
        ),
    ]