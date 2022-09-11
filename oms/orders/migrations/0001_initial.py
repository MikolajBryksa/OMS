# Generated by Django 4.1.1 on 2022-09-09 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('seller', models.CharField(choices=[('Mark', 'Mark'), ('Natalie', 'Natalie'), ('Joanna', 'Joanna')], max_length=20)),
                ('customer', models.EmailField(max_length=260)),
                ('designer', models.CharField(choices=[('Miki', 'Miki'), ('Ola', 'Ola')], max_length=20)),
                ('status', models.CharField(choices=[('New', 'New'), ('Urgent', 'Urgent'), ('Drawing', 'Drawing'), ('Incomplete', 'Incomplete'), ('Designed', 'Designed'), ('Evaluation', 'Evaluation'), ('Improvement', 'Improvement'), ('Accepted', 'Accepted'), ('Production', 'Production'), ('Packed', 'Packed'), ('Sent', 'Sent')], default='New', max_length=20)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('material', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('depth', models.IntegerField(blank=True, null=True)),
                ('fastening', models.CharField(max_length=30)),
                ('hole', models.CharField(blank=True, max_length=20, null=True)),
                ('rounding', models.CharField(blank=True, max_length=10, null=True)),
                ('mark', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
