# Generated by Django 4.1.2 on 2022-11-15 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_rename_wieght_pr_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.plan')),
            ],
        ),
    ]