# Generated by Django 5.0.4 on 2024-04-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likedislike',
            name='dislike_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='likedislike',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
