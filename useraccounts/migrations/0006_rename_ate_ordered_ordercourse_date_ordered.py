# Generated by Django 3.2.4 on 2021-06-14 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0005_auto_20210614_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordercourse',
            old_name='ate_ordered',
            new_name='date_ordered',
        ),
    ]
