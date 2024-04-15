# Generated by Django 5.0.4 on 2024-04-10 17:20

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartnfc', '0004_alter_wallet_dual_account_paynowpayment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='paynowpayment',
            name='browser_url',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='paynowpayment',
            name='paid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='paynowpayment',
            name='poll_url',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='paynowpayment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('trans_id', models.CharField(blank=True, max_length=50, unique=True)),
                ('amount_deposit', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('currency', models.CharField(blank=True, max_length=50)),
                ('source', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wallet', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit', to='smartnfc.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('trans_id', models.CharField(blank=True, max_length=50, unique=True)),
                ('amount_deposit', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('currency', models.CharField(blank=True, max_length=50)),
                ('source', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wallet', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='withdraw', to='smartnfc.wallet')),
            ],
        ),
    ]