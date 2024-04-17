# Generated by Django 4.2.11 on 2024-04-17 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_remove_position_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_name', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.position')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
