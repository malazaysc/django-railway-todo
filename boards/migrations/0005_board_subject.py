# Generated by Django 4.2.1 on 2023-05-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_alter_todo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='subject',
            field=models.CharField(default='generic todo list', max_length=255),
            preserve_default=False,
        ),
    ]
