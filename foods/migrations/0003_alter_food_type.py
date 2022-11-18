# Generated by Django 4.1.1 on 2022-09-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_food_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type',
            field=models.CharField(choices=[('breakfast', 'صبحانه'), ('drinks', 'نوشیدنی'), ('dinner', 'شام'), ('lunch', 'نهار')], default='dinner', max_length=10, verbose_name='نوع غذا'),
        ),
    ]