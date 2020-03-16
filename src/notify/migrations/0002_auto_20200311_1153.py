# Generated by Django 3.0.4 on 2020-03-11 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifies', to='notify.Bank', verbose_name='Bank'),
        ),
    ]
