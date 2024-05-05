# Generated by Django 5.0.3 on 2024-03-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]