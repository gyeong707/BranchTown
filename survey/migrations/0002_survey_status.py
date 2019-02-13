# Generated by Django 2.1.5 on 2019-02-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='status',
            field=models.CharField(choices=[('o', 'ongoing'), ('c', 'complete')], default='o', max_length=1),
            preserve_default=False,
        ),
    ]