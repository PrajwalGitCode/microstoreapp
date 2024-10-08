# Generated by Django 5.0.7 on 2024-09-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_graphic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphic',
            name='image',
            field=models.ImageField(default='gra_images/w_5.png', upload_to='gra_images/'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='image',
            field=models.ImageField(default='mob_images/w_5.png', upload_to='mob_images/'),
        ),
    ]
