# Generated by Django 3.0.6 on 2020-06-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmvpinterface', '0002_auto_20200621_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metric',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='commit',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='time commit created'),
        ),
    ]