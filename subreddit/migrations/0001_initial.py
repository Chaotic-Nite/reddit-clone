# Generated by Django 3.2.5 on 2021-07-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_moderator', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubReddit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(max_length=200)),
                ('moderator', models.ManyToManyField(related_name='moderator', to='subreddit.Moderator')),
            ],
        ),
    ]
