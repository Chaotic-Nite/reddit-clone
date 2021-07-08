# Generated by Django 3.2.5 on 2021-07-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0003_post_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='votes',
        ),
    ]
