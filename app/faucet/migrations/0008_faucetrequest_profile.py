# Generated by Django 2.0.3 on 2018-04-13 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0051_auto_20180405_0806'),
        ('faucet', '0007_auto_20180427_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucetrequest',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='faucet_requests', to='dashboard.Profile'),
        ),
    ]
