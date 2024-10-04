# Generated by Django 5.1.1 on 2024-09-04 15:08

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('object_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=3)),
                ('orientation', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=3)),
                ('scale', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('joint_angles', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=None)),
                ('robot_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_library.referencerobot')),
                ('scene_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scene_manager.scene')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=3)),
                ('orientation', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=3)),
                ('scale', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('color', models.CharField(max_length=7)),
                ('object_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_library.referenceobject')),
                ('scene_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scene_manager.scene')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]