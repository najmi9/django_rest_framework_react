# Generated by Django 3.1.1 on 2020-09-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image', models.URLField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updtedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
