# Generated by Django 4.0.3 on 2022-03-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0009_cap_capdescription_cap_capname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('storeID', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('storeName', models.CharField(max_length=50)),
                ('storePhone', models.CharField(max_length=50)),
                ('storeAddress', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='ADDRESS',
            new_name='customerAddress',
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='ID',
            new_name='customerID',
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='PHONE',
            new_name='customerPhone',
        ),
        migrations.RenameField(
            model_name='drivers',
            old_name='ADDRESS',
            new_name='driverAddress',
        ),
        migrations.RenameField(
            model_name='drivers',
            old_name='ID',
            new_name='driverID',
        ),
        migrations.RenameField(
            model_name='drivers',
            old_name='USER',
            new_name='driverName',
        ),
        migrations.RenameField(
            model_name='drivers',
            old_name='PHONE',
            new_name='driverPhone',
        ),
        migrations.RenameField(
            model_name='orderdetails',
            old_name='Order',
            new_name='orderID',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='USER',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderTime',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderTotal',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='Meal',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='Subtotal',
        ),
        migrations.AddField(
            model_name='customers',
            name='customerName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='customerID',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='orderAccountNumber',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='storeID',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='productID',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meals',
            name='PRICE',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='productPrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='productQuantity',
            field=models.IntegerField(default=0),
        ),
    ]
