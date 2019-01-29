# Generated by Django 2.1.5 on 2019-01-23 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190123_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'withdrawn')], default='d', max_length=1),
            preserve_default=False,
        ),
    ]