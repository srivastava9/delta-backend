# Generated by Django 2.1.7 on 2020-04-02 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200402_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_branch', to='utilities.Branch'),
        ),
    ]