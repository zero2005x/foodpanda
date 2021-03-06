# Generated by Django 4.0.2 on 2022-02-24 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_test_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Venue Name')),
                ('venue_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
