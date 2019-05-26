# Generated by Django 2.2.1 on 2019-05-26 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40)),
                ('image', models.ImageField(upload_to='image/')),
                ('likes', models.IntegerField()),
            ],
        ),
    ]
