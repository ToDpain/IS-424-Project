# Generated by Django 4.2 on 2023-05-19 04:39

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
                ('year', models.IntegerField()),
                ('model', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
    ]
