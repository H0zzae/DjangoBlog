# Generated by Django 3.1 on 2020-08-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200810_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='newCategory', max_length=50, null=True, verbose_name='카테고리 제목'),
        ),
    ]
