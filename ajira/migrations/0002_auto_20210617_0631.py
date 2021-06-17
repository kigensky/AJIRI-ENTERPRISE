# Generated by Django 3.2.4 on 2021-06-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajira', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.CharField(choices=[('Human Resource', 'Human Resource'), ('Marketing', 'Marketing'), ('Accounting', 'Accounting')], default='Marketing', max_length=20)),
                ('address', models.TextField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('job_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='ShoppingItem',
        ),
    ]
