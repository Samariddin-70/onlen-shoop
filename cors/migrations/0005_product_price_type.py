# Generated by Django 5.2.1 on 2025-06-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cors', '0004_brand_alter_category_managers_alter_user_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_type',
            field=models.CharField(choices=[('UZS', 'Uzbek so`mi'), ('USD', 'Aqsh dollori'), ('RUB', 'Rossia rubili')], default='UZS', max_length=3),
        ),
    ]
