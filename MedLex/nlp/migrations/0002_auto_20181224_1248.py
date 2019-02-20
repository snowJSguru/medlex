# Generated by Django 2.1.4 on 2018-12-24 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='redaction',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]
