# Generated by Django 4.2.1 on 2023-05-16 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_alter_todo_options_todo_ordering_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='todo',
            name='unique_ordering',
        ),
    ]
