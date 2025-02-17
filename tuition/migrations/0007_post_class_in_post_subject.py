# Generated by Django 5.0.3 on 2024-03-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0006_class_in_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='class_in',
            field=models.ManyToManyField(related_name='Class_in', to='tuition.class_in'),
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.ManyToManyField(related_name='Subjects_added', to='tuition.subject'),
        ),
    ]
