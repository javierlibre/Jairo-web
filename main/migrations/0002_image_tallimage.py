# Generated by Django 4.1.2 on 2023-02-26 18:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tallImage',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_tall.jpg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1618, 2878], upload_to='tall'),
        ),
    ]
