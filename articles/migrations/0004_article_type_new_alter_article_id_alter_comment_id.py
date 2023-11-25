# Generated by Django 4.1.3 on 2022-11-13 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='type_new',
            field=models.CharField(choices=[('Sport', 'Sport'), ('Jahon', 'Jahon')], default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
