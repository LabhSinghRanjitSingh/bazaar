# Generated by Django 2.0.7 on 2018-09-30 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wholesale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainText', models.CharField(blank=True, max_length=100)),
                ('subText', models.CharField(blank=True, max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wholesale.Book')),
            ],
        ),
    ]
