# Generated by Django 5.0.3 on 2025-02-23 11:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bdate', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-')], max_length=100)),
                ('profession', models.CharField(choices=[('Studen', 'Student'), ('Tutor', 'Tutor')], max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=13)),
                ('bio', models.TextField()),
                ('nationality', models.CharField(max_length=30)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Christian', 'Christian')], max_length=50)),
                ('profile_pic', models.ImageField(default='default.jpg', upload_to='media/images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
