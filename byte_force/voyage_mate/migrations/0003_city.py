# Generated by Django 5.1.3 on 2024-11-16 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage_mate', '0002_alter_destination_description_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
    ]
