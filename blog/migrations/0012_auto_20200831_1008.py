# Generated by Django 2.2.14 on 2020-08-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_resume_skillfield4'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='skillDescription1',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='skillDescription2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='skillDescription3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='skillDescription4',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
