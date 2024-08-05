# Generated by Django 4.2.14 on 2024-08-05 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beer_card', '0002_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beer',
            options={'ordering': ['beer_name']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_on']},
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.AddField(
            model_name='review',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='beer',
            name='rating',
            field=models.FloatField(),
        ),
    ]
