# Generated by Django 4.2.1 on 2023-06-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0010_alter_movie_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
