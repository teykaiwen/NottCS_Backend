# Generated by Django 2.0.2 on 2018-02-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AzureADUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('student_id', models.PositiveIntegerField(blank=True, null=True)),
                ('library_no', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
