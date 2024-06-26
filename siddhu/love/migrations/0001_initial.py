# Generated by Django 5.0.6 on 2024-06-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=15)),
                ('alternate_no', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField()),
                ('company_name', models.CharField(max_length=255)),
                ('model_no', models.CharField(max_length=255)),
                ('physical_condition', models.CharField(max_length=255)),
                ('estimated_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imei_1', models.CharField(max_length=15, unique=True)),
                ('imei_2', models.CharField(blank=True, max_length=15, null=True, unique=True)),
            ],
        ),
    ]
