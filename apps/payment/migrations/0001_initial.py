# Generated by Django 4.1 on 2023-02-11 23:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=35)),
                ('email_address', models.EmailField(max_length=254)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateTimeField()),
                ('ref_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
