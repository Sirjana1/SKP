# Generated by Django 5.1.1 on 2024-11-02 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0006_feedback_feedback_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='id',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='BolckPostCreaterDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(help_text=' * First Name Field Mandatory ', max_length=100, verbose_name='First Name:')),
                ('lname', models.CharField(default=False, max_length=100)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.blogpost')),
            ],
        ),
    ]
