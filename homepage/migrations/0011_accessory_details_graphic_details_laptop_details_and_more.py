# Generated by Django 5.0.7 on 2024-09-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_mobile_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='details',
            field=models.TextField(default='coming soon'),
        ),
        migrations.AddField(
            model_name='graphic',
            name='details',
            field=models.TextField(default='coming soon'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='details',
            field=models.TextField(default='coming soon'),
        ),
        migrations.AddField(
            model_name='processor',
            name='details',
            field=models.TextField(default='coming soon'),
        ),
        migrations.AddField(
            model_name='watches',
            name='details',
            field=models.TextField(default='coming soon'),
        ),
    ]
