# Generated by Django 2.1.7 on 2020-04-27 14:49

from django.db import migrations, models
import utilities.models.website


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0004_skill_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='website',
            options={'verbose_name_plural': 'Websites'},
        ),
        migrations.AlterField(
            model_name='website',
            name='website_logo',
            field=models.ImageField(blank=True, null=True, upload_to='social_link_logo/', validators=[utilities.models.website.validate_image]),
        ),
    ]
