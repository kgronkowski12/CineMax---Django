# Generated by Django 4.2.1 on 2023-05-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0002_remove_comment_email_comment_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
