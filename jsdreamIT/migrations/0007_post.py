# Generated by Django 3.2.8 on 2021-12-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsdreamIT', '0006_auto_20211206_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='blog')),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
