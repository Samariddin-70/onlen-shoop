# Generated by Django 5.2.1 on 2025-06-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cors', '0002_category_remove_user_ful_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ful_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Isim Sharif'),
        ),
    ]
