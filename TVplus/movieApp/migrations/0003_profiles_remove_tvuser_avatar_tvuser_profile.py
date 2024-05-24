# Generated by Django 4.2.11 on 2024-05-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0002_alter_tvuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Profil ismi')),
                ('avatar', models.ImageField(upload_to='Users/Avatars/', verbose_name='Profil Fotoğrafı')),
            ],
        ),
        migrations.RemoveField(
            model_name='tvuser',
            name='avatar',
        ),
        migrations.AddField(
            model_name='tvuser',
            name='profile',
            field=models.ManyToManyField(to='movieApp.profiles', verbose_name='profiller'),
        ),
    ]
