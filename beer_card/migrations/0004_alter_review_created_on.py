# Generated by Django 4.2.14 on 2024-08-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer_card', '0003_alter_beer_options_alter_review_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
