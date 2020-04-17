# Generated by Django 2.1.7 on 2020-04-17 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0002_auto_20200415_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(db_index=True, max_length=128)),
                ('hash', models.CharField(blank=True, db_index=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]
