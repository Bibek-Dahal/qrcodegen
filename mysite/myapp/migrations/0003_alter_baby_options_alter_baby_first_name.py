# Generated by Django 4.2.3 on 2023-08-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_baby_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baby',
            options={'ordering': ['first_name'], 'verbose_name': 'baby', 'verbose_name_plural': 'babies'},
        ),
        migrations.AlterField(
            model_name='baby',
            name='first_name',
            field=models.CharField(max_length=15, verbose_name='first name'),
        ),
    ]