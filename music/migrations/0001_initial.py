# Generated by Django 3.0.4 on 2020-04-14 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=50)),
                ('album_title', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=50)),
                ('album_logo', models.ImageField(blank=True, upload_to=music.models.user_directory_path_image)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=100)),
                ('audio_file', models.FileField(blank=True, upload_to=music.models.user_directory_path_music)),
                ('is_favourite', models.BooleanField(default=False)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
