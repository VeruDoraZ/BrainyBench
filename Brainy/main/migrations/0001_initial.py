# Generated by Django 4.2.7 on 2023-12-02 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('countries', models.CharField(choices=[('thailand', 'thai'), ('southafrica', 'south'), ('russia', 'ru'), ('norway', 'nor')], default='', max_length=20)),
                ('img', models.ImageField(default='noimage.jpg', upload_to='quiz_image')),
            ],
        ),
    ]