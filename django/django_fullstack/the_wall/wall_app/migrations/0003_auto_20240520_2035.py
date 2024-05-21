# Generated by Django 2.2.4 on 2024-05-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0002_remove_message_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(),
        ),
    ]