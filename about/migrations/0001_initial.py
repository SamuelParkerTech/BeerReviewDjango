# Generated by Django 4.2.14 on 2024-08-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('about_pub', models.TextField()),
                ('about_site', models.TextField()),
            ],
        ),
    ]
