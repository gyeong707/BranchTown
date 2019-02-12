# Generated by Django 2.1.5 on 2019-02-12 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', '객관식'), ('2', '주관식'), ('3', '단답식')], max_length=10)),
                ('question', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Multiple_Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=30)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Field')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(to='tag.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='field',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
        ),
    ]