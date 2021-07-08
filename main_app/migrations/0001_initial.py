# Generated by Django 3.2.5 on 2021-07-06 19:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('moderators', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('posts', models.ManyToManyField(blank=True, to='post_app.Post')),
            ],
        ),
    ]