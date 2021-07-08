# Generated by Django 3.2.5 on 2021-07-08 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dislikes',
            new_name='downvote',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='upvote',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]