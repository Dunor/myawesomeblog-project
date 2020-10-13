# Generated by Django 3.1.1 on 2020-10-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_tittle', models.CharField(max_length=300)),
                ('post_date', models.DateTimeField()),
                ('post_text', models.TextField()),
                ('post_image', models.ImageField(upload_to='post_images/')),
            ],
        ),
    ]