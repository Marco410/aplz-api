# Generated by Django 5.0.1 on 2024-12-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('DeletedAt', models.DateTimeField(blank=True, null=True)),
                ('date', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('loanId', models.IntegerField(blank=True, null=True)),
                ('merchantId', models.IntegerField(blank=True, null=True)),
                ('products', models.CharField(blank=True, max_length=255, null=True)),
                ('branchId', models.IntegerField(blank=True, null=True)),
                ('sellsAgentId', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
