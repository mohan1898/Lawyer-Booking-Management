# Generated by Django 3.2.7 on 2022-04-13 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lawyerapp', '0002_auto_20220408_1425'),
        ('clientapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_lawyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Book_lawyer',
            },
        ),
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('rating', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientapp.client')),
                ('lawyer', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='clientapp.book_lawyer')),
            ],
            options={
                'db_table': 'client_feedback',
            },
        ),
        migrations.AddField(
            model_name='book_lawyer',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientapp.client'),
        ),
        migrations.AddField(
            model_name='book_lawyer',
            name='lawyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawyerapp.lawyer'),
        ),
    ]