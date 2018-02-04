# Generated by Django 2.0.1 on 2018-02-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('photo', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('photo', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('production_date', models.DateField()),
                ('description', models.CharField(max_length=10000)),
                ('rate', models.FloatField()),
                ('trailer_url', models.CharField(max_length=1000)),
                ('movie_logo', models.CharField(default='', max_length=1000)),
                ('genre', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('photo', models.CharField(default='', max_length=1000)),
                ('movies', models.ManyToManyField(to='movies.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='movies',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
    ]
