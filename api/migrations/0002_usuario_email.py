# Generated by Django 5.0.6 on 2024-06-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
