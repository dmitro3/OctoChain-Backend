# Generated by Django 4.1.5 on 2023-12-30 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hedge_bot', '0008_exchange_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HedgeBotBlacklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tick', models.CharField(max_length=255)),
                ('until_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('hedge_exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blacklist_hedge_exchange', to='hedge_bot.exchange')),
                ('spot_exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blacklist_spot_exchange', to='hedge_bot.exchange')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]