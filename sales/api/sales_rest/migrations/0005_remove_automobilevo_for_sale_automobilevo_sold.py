# Generated by Django 4.0.3 on 2023-03-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0004_automobilevo_for_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automobilevo',
            name='for_sale',
        ),
        migrations.AddField(
            model_name='automobilevo',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
