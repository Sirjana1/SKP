# Generated by Django 5.1.1 on 2024-10-31 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_quantity', models.PositiveIntegerField(default=0)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('last_added_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='GroceryItem',
        ),
    ]
