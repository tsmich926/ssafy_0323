# Generated by Django 3.2.18 on 2023-03-21 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.CharField(default='aaa', max_length=10),
            preserve_default=False,
        ),
    ]
