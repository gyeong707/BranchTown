# Generated by Django 2.1.5 on 2019-02-13 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20190214_0225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multiple_choice',
            old_name='q1',
            new_name='choice1',
        ),
        migrations.RenameField(
            model_name='multiple_choice',
            old_name='q2',
            new_name='choice2',
        ),
        migrations.RenameField(
            model_name='multiple_choice',
            old_name='q3',
            new_name='choice3',
        ),
    ]
