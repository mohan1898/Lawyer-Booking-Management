# Generated by Django 3.2.7 on 2022-04-14 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lawyerapp', '0002_auto_20220408_1425'),
        ('clientapp', '0002_auto_20220413_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='lawyer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lawyerapp.lawyer'),
        ),
    ]
