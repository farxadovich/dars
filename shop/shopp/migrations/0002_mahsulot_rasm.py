# Generated by Django 3.2.2 on 2021-05-31 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='rasm',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
