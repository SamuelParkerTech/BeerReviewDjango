from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('beer_card', '0003_alter_beer_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer',
            name='rating',
        ),
    ]