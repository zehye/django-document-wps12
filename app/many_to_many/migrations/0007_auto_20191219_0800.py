# Generated by Django 3.0 on 2019-12-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0006_auto_20191219_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramuser',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='many_to_many.Relation', to='many_to_many.InstagramUser'),
        ),
    ]