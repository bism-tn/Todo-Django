# Generated by Django 5.1.6 on 2025-03-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_alter_taskmodel_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
