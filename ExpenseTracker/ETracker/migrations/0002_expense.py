# Generated by Django 5.1.6 on 2025-02-21 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ETracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='ETracker.category')),
            ],
        ),
    ]
