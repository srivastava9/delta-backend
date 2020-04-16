# Generated by Django 2.1.7 on 2020-04-16 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20200416_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='work_type',
            field=models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time')], default='part time', max_length=255, verbose_name='Type of Work'),
        ),
    ]
