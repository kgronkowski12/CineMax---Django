# Generated by Django 4.2.1 on 2023-06-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0006_alter_comment_movie_id_alter_repertoire_movie_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
