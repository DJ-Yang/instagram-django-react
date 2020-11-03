# Generated by Django 3.1.2 on 2020-11-03 13:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follower_set',
            field=models.ManyToManyField(blank=True, related_name='_user_follower_set_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following_set',
            field=models.ManyToManyField(blank=True, related_name='_user_following_set_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='24px * 24px 크기의 png/jpg 파일을 업로드해주세요.', upload_to='accounts/profile/%Y/%m/%d'),
        ),
    ]
