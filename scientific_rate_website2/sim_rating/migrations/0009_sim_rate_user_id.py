# Generated by Django 3.0.8 on 2020-10-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim_rating', '0008_remove_sim_rate_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sim_rate',
            name='user_id',
            field=models.CharField(help_text='User ID', max_length=20, null=True),
        ),
    ]
