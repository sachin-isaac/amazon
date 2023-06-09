# Generated by Django 4.1 on 2023-06-09 18:23
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_remove_orderscancelled_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderz',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out For Shipping', 'Out For Shipping'), ('Completed', 'Completed'), ('Cancelled', 'Cancel')], default='Pending', max_length=50)),
                ('tracking_no', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('shipping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shipping')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
