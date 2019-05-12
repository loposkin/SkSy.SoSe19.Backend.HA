# Generated by Django 2.2 on 2019-05-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(max_length=160)),
                ('deadline', models.DateTimeField(verbose_name='deadline')),
                ('progress', models.FloatField(verbose_name='progress')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
