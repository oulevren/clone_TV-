# Generated by Django 4.2.11 on 2024-05-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0003_profiles_remove_tvuser_avatar_tvuser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='avatar',
            field=models.ImageField(default='static/Static/profile/default_avatar.png', upload_to='Users/Avatars/', verbose_name='Profil Fotoğrafı'),
        ),
    ]