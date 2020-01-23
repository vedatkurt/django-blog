# Generated by Django 2.0.3 on 2020-01-19 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200112_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='Isim')),
                ('comment_content', models.CharField(max_length=200, verbose_name='comment')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='Comment Create Date')),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article', verbose_name='comment')),
            ],
        ),
    ]
