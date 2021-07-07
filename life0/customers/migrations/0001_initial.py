# Generated by Django 3.2.4 on 2021-07-06 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='customers/profiles/avatars/')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True)),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('zip', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
