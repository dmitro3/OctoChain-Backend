# Generated by Django 4.1.5 on 2023-12-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hedge_bot', '0006_hedgebottx_hedge_cost_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='future',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='exchange',
            name='spot',
            field=models.BooleanField(default=True),
        ),
    ]
