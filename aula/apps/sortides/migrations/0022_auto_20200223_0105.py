# Generated by Django 2.2.6 on 2020-02-23 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortides', '0021_auto_20200216_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortida',
            name='tipus_de_pagament',
            field=models.CharField(choices=[('NO', 'No cal pagament'), ('EF', 'En efectiu'), ('ON', 'Online a través del djAu'), ('EB', "Al caixer de l'entitat bancària")], default='NO', help_text='Quin serà el tipus de pagament predominant', max_length=2),
        ),
    ]
