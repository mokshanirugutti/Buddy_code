# Generated by Django 4.2.4 on 2023-08-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CODE_APP', '0002_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='general', max_length=200),
        ),
    ]
