# Generated by Django 2.0 on 2018-02-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_delete_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='photo',
            field=models.CharField(default='', max_length=1000),
        ),
    ]