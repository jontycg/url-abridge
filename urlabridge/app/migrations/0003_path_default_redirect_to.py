# Generated by Django 2.2.6 on 2019-10-18 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191011_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='path',
            name='default_redirect_to',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]