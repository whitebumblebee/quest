# Generated by Django 2.1.4 on 2019-04-10 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account',
            field=models.OneToOneField(help_text='The account to which this user belongs', on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Account'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(help_text='The user to whom this profile belongs', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
