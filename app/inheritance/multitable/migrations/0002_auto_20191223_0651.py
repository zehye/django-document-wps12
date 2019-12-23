# Generated by Django 3.0 on 2019-12-23 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multitable', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place1',
            options={'ordering': ['name'], 'verbose_name': '장소1', 'verbose_name_plural': '장소 목록'},
        ),
        migrations.AddField(
            model_name='restaurant1',
            name='near_place',
            field=models.ManyToManyField(related_name='restaurant_set', related_query_name='restaurant1_by_near_places', to='multitable.Place1'),
        ),
        migrations.AlterField(
            model_name='restaurant1',
            name='place1_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='restaurant1', related_query_name='restaurant1_by_oto', serialize=False, to='multitable.Place1'),
        ),
    ]
