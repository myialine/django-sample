# Generated by Django 3.0.8 on 2020-07-31 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current_status', models.CharField(choices=[('Y', 'Active'), ('N', 'Not Active')], default='N', max_length=1)),
            ],
        ),
    ]
