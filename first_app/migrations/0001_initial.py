# Generated by Django 4.1.7 on 2023-03-21 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
