# Generated by Django 3.0.8 on 2020-08-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ques', models.CharField(max_length=150)),
                ('ans', models.TextField()),
                ('author', models.CharField(default='Admin', max_length=20)),
                ('add', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('phone', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
    ]