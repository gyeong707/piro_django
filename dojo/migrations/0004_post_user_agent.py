# Generated by Django 2.1.5 on 2019-02-02 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0003_auto_20190202_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_agent',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
