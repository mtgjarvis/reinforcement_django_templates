# Generated by Django 2.2.3 on 2019-07-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('pin', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
            ],
        ),
    ]
