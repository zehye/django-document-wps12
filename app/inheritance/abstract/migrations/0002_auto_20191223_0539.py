# Generated by Django 3.0 on 2019-12-23 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abstract', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '학생', 'verbose_name_plural': '학생 목록'},
        ),
        migrations.CreateModel(
            name='Childb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m2m', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abstract.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChildA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m2m', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abstract.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]