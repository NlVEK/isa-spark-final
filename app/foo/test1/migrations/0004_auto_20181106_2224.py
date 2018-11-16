# Generated by Django 2.1 on 2018-11-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0003_thing'),
    ]

    operations = [
        migrations.CreateModel(
            name='auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('auth', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.AddField(
            model_name='person',
            name='pwd',
            field=models.CharField(default='123456', max_length=32),
        ),
        migrations.AddField(
            model_name='person',
            name='user_name',
            field=models.CharField(default='abcdef', max_length=30),
        ),
    ]