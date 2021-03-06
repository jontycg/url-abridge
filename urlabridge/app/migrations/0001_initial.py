# Generated by Django 2.2.6 on 2019-10-11 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redirect_from', models.CharField(max_length=5000)),
                ('redirect_to', models.CharField(max_length=1000)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Domain')),
            ],
        ),
    ]
