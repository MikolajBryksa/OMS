# Generated by Django 4.1.1 on 2022-09-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_item_thickness_alter_item_material_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('White', 'White'), ('Black', 'Black'), ('Transparent', 'Transparent'), ('Custom', 'Custom')], max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='dimensions',
            field=models.CharField(blank=True, choices=[('Outside', 'Outside'), ('Inside', 'Inside')], default='Outside', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='fastening',
            field=models.CharField(choices=[('Pin', 'Pin'), ('Magnet', 'Magnet'), ('Glue', 'Glue'), ('Holes', 'Holes'), ('Without', 'Without'), ('Custom', 'Custom')], max_length=30),
        ),
        migrations.AlterField(
            model_name='item',
            name='mark',
            field=models.CharField(choices=[('Print', 'Print'), ('Engraver', 'Engraver'), ('Foil', 'Foil'), ('Sticker', 'Sticker'), ('Without', 'Without'), ('Custom', 'Custom')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='thickness',
            field=models.CharField(choices=[('0,5', '0,5'), ('0,8', '0,8'), ('1,6', '1,6'), ('2', '2'), ('3', '3'), ('5', '5'), ('Other', 'Other')], max_length=10),
        ),
    ]
