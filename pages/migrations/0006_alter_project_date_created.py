# Generated by Django 4.0.6 on 2022-07-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_project_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
